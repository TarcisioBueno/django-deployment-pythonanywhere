from django.urls import path
from . import views


app_name = 'finance'
#<slug:slug>/<int:week_days>/
urlpatterns = [

	path('checkout1/<int:course_choice>/', views.checkout1,name='checkout1'),	
	path('check_prices/',views.check_prices,name='check_prices'),
	path('checkout3/<int:package>/',views.checkout3,name='checkout3')


]