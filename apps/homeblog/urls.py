from django.urls import path
from homeblog import views


urlpatterns = [

   	path('', views.home, name='home'),
	 
   
]
