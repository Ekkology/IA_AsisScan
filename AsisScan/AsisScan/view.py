from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def login(request):
        return render(request,"login_main.html")

def control(request):
        return render(request,"control.html")

def configuraciones(request):
        return render (request,"configuracion.html")

def  video_imagen(request):
        return render(request,"video_imagen.html")


def home(request):
        return render(request, 'home.html')