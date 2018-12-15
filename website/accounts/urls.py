from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('create_account/',views.create_user,name='create_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user, name='logout_user'),
    path('number_token_form/',views.number_token_form,name='number_token_form'),
    path('email_confirm_done/',views.email_confirm_done,name='email_confirm_done'),
    path('email_confirm_fail/',views.email_confirm_fail,name='email_confirm_fail'),
    
    

]
