from django.urls import path
from plataforma import views

app_name = 'plataforma'

urlpatterns = [	
	path('',views.plataforma_index,name='plataforma_index'),
	path('course_content/<int:course_id>/<slug:slug>/',views.course_content,name='course_content'),
	path('topic_content/<slug:course_link>/<int:topic_id>/<slug:slug>/',views.topic_content, name='topic_content'),
	path('quiz/<int:topic_id>/<slug:slug>/',views.quiz, name='quiz'),
	path('word_list/',views.word_list,name="word_list"),
	path('user_page/',views.user_page,name="user_page"),
	
]