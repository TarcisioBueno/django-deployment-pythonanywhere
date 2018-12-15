from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from blog.models import Post
from django.core.mail import send_mail
import random


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            url = request.POST.get('next','blog:blog_list')
            if url != '':
                return redirect(url)
            else:
                return redirect('blog:blog_list')
        else:
            context = {'error_message':'Username ou Senha está incorreto ou você não tem permissões '}
            return render(request,'registration/login.html',context)
    else:
        return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('blog:blog_list')


def create_user(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']
        if password1 != password2:
            context={'error_message':'Duas Senhas Diferentes'}
            return render(request, 'registration/create_user.html',context)
        else:
            digits = 0
            for i in password1:
                digits +=1
            if digits < 6:
                context={'error_message':'Senha precisa ter no mínimo 6 dígitos'}
                return render(request, 'registration/create_user.html',context)
            username = request.POST['username']
            digits = 0
            for i in username:
                digits +=1
                if i == ' ':
                    context={'error_message':'Username inválido, não pode ter espaço'}
                    return render(request, 'registration/create_user.html',context)
            if digits < 5:
                context={'error_message':'Username precisa ter no mínimo 5 dígitos'}
                return render(request, 'registration/create_user.html',context)
            email = request.POST['email']
            if User.objects.filter(username=username).exists():
                context={'error_message':'Username já existe'}
                return render(request, 'registration/create_user.html',context)
            elif User.objects.filter(email=email).exists():
                context={'error_message':'Já existe um usuário com o mesmo email'}
                return render(request, 'registration/create_user.html',context)
            else:
                User.objects.create_user(username,email,password1)
                user = authenticate(request,username=username,password=password1)
                if user is not None:
                    login(request,user)
                    token = random.randint(10000,99999)
                    user.profile.email_token = token                
                    user.save()
                    if send_token_email(request,email,token):
                        return redirect('accounts:number_token_form')
    else:
        return render(request, 'registration/create_user.html')


def number_token_form(request):
    if request.method == 'POST':
        username_id = request.POST['id']
        form_token = request.POST['token']
        user = User.objects.get(pk=username_id)
        user_token = user.profile.email_token 
        if int(form_token)==int(user_token):
            user.profile.email_token = random.randint(10000,99999)
            user.profile.email_status = True
            user.save()
            return redirect('finance:check_prices')
        else:
            context = {'error_message':'Esse não é o código correto. Por favor tente mais uma vez.'}
            return render(request, 'registration/number_token_form.html',context)
    else:
        return render(request, 'registration/number_token_form.html')

def email_confirm_done(request):
    return render(request,'registration/email_confirm_done.html')

def email_confirm_fail(request):
    return render(request,'registration/email_confirm_fail.html')

def send_token_email(request,email,token):
    send_mail(
    'Confirmação de email - Zero To Hero English',
    'Olá, o código de confirmação de email é {}, coloque esse código no formulário para que o seu email seja confirmado. O time Zero To Hero English agradece.'.format(token),
    'zerotoheroenglish.com@gmail.com',
    [email],
    fail_silently=False,
    )
    return True


