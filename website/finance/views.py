from django.shortcuts import render,redirect
from accounts.models import Teacher
from django.contrib.auth.decorators import login_required
import datetime



'''
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    email_token = models.IntegerField(default=0)
    email_status = models.BooleanField(default=False)
    class_time = models.CharField(max_length=500)  
    teacher = models.CharField(max_length=500)    
 '''
@login_required(login_url='/accounts/login_user/') 
def checkout1(request,course_choice):
	if request.method == 'POST':
		user = request.user
		teacher_id = request.POST['teacher_id']
		time_hour = request.POST['time_selected1']
		time_day = request.POST['timeday1']
		teacher = Teacher.objects.get(pk=teacher_id)
		user.profile.teacher = teacher.name
		now = datetime.datetime.now()
		user.profile.class_time = str(now) + " - " + time_day + " - " + time_hour
		user.save()
		payment = False
		message = "A sua mensagem foi salva no nosso sistema. Enviaremos um email respondendo em breve."
		context = {'message':message,'payment':payment}				
		return render(request,'finance/checkout2.html',context)
	else:
		teachers = Teacher.objects.all()
		if course_choice == 1:
			message = False
		else:
			message = True
		context = {'teachers':teachers,'message':message}
		return render(request,'finance/checkout1.html',context)

@login_required(login_url='/accounts/login_user/') 
def checkout3(request,package):
	if package == 1:
		message = True
		course = 'Assinante Premium Zero To Hero English'
	else:
		message = False
		course = 'Assinante Zero To Hero English'
	context = {'message':message,'course':course}
	return render(request,'finance/checkout3.html',context)

@login_required(login_url='/accounts/login_user/') 
def check_prices(request):
	return render(request,'finance/prices.html')