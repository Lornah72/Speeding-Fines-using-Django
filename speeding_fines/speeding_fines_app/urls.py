from django.urls import path
from . import views


urlpatterns = [

    path('login_officer',views.login_officer,name= 'login_officer'),
    path('home',views.home,name= 'home'),
    
    
    
    
]