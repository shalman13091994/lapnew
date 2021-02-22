from django.shortcuts import render
from .models import person
from django.http import HttpResponse

def homepage(request):
    allpost=person.objects.all()

    return render(request,'home.html',{'posts':allpost})

def welcome(request):
  nam =request.POST['uname']
  pas=request.POST['psw']

  mod=nam+' '+pas

  return render(request,'welcome.html',{'final':mod})

def password(request):
    return render(request,'password.html')

