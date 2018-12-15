from django.shortcuts import render,redirect
from .models import Course,Category,Topic,Word_list
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def is_student(user):
    return user.profile.is_student == True

@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student,login_url='/finance/check_prices/')
def plataforma_index(request):
    courses = Course.objects.order_by('id')
    context = {'courses':courses}  
    return render(request,'plataforma/plataforma_index.html',context)

@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student,login_url='/finance/checkout1/')#redirect to checkout page
def course_content(request,course_id,slug):
	course = Course.objects.get(pk=course_id)
	context = {'course':course}
	return render(request, 'plataforma/course_content.html',context)

@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student)#redirect to checkout page
def topic_content(request,course_link,topic_id, slug):
	topic = Topic.objects.get(pk=topic_id)
	context = {'topic':topic}
	return render(request,'plataforma/topic_content.html',context)
    
@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student,login_url='/finance/check_prices/')#redirect to checkout page
def quiz(request,topic_id,slug):
    if request.method == 'POST':
        topic = Topic.objects.get(pk=topic_id)
        question_list = topic.question_set.all()
        i=1
        corrects = []
        incorrects = []
        for question in question_list:
            selected_option = request.POST['option{}'.format(i)]
            if question.right_option == selected_option:
                corrects.append(question)
            else:
                incorrects.append(question)
            i+=1
        percentage = float(len(corrects)/(i-1)*100)
        if percentage == 0:
            message = 'Você errou todas as questões, estude o conteúdo novamente e depois disso faça o questionário de novo.'
        elif percentage < 70.0:
            message = 'Você acertou menos de 70 %, reveja o conteúdo, pratique mais e volte a esse questionário para melhorar o seu resultado.'
        elif percentage == 100.0:
            message = 'Parabéns! Um ótimo resultado, continue assim!'
        elif percentage >= 70.0:
            message = 'Muito bem! Você ainda pode melhorar, mas o seu desempenho já está muito bom.'
        
        context = {'corrects':corrects,'incorrects':incorrects,'topic':topic,'percentage':percentage,'message':message}
        return render(request,'plataforma/quiz_result.html',context)
    else:
        topic = Topic.objects.get(pk=topic_id)
        context = {'topic':topic}
        return render(request,'plataforma/quiz.html',context)

@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student,login_url='/finance/check_prices/')#redirect to checkout page
def word_list(request):
    word_lists = Word_list.objects.order_by('list_date')
    context = {'word_lists':word_lists}
    return render(request,'plataforma/word_list.html', context)

@login_required(login_url='/accounts/login_user/')      
@user_passes_test(is_student,login_url='/finance/check_prices/')#redirect to checkout page
def user_page(request):
    return render(request,'plataforma/user_page.html')
    







