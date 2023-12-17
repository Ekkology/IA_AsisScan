from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def login(request):
        return render(request,"login_main.html")



def configuraciones(request):
        return render (request,"configuracion.html")


def home(request):
        return render(request, 'home.html')


#parte de sebastian 
from django.shortcuts import  render
from Datos_Control_Asistencia.models import persona
from django.http import JsonResponse

def index(request):
        return render(request, 'index.html')

def login(request):
        return render(request,"login_main.html")

def control(request):
        return render(request,"control.html")

def UserProfile(request):
        Usuario = persona.objects.get(id_persona=1)

        return render(request,
                      "UserProfile.html",
                      {'User': Usuario})
### fin de la parte de sebastian