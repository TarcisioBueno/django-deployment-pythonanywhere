from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from datetime import date, timedelta


class Teacher(models.Model):
    img = models.URLField(blank=True)
    name = models.CharField(max_length=200)    
    description = models.CharField(max_length=500,blank=True)	
        
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    email_token = models.IntegerField(default=0)
    email_status = models.BooleanField(default=False)
    class_time = models.CharField(max_length=500,blank=True)  
    teacher = models.CharField(max_length=500,blank=True) 
    releases = models.TextField(blank=True)   

       
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()	
    
