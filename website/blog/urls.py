from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[

    path('',views.content_list,name='blog_list'),
    path('artigos/<int:content_id>/<slug:slug>/',views.content_detail, name='content_detail'),
    path('email_list',views.email_list,name='email_list'),




]
