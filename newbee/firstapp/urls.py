from django.urls import path
from.views import homepage,welcome,password

urlpatterns=[
    path('',homepage,name='home'),
    path('welcome',welcome,name='welcome'),
    path('password',password,name='pass'),
    path('home',homepage,name='home')

]