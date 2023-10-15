from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    if request.method == "GET":
        print("enviando formulario")
        return render(request, "index.html")
    else:
        if request.POST["contraseña"] == request.POST["confirmar_contraseña"]:
            try:
                # registrar en la base de datos
                user = User.objects.create_user(
                    username=request.POST["nombre"], password=request.POST["contraseña"]
                )
                user.save()
                login(request,user)
                return redirect("control")
            except:
                return render(
                    request,
                    "index.html",
                    {"error": "El Usuario ya existe, prueba con otro"},
                )

        return render(
            request,
            "index.html",
            {"error": "Las  contraseñas no son iguales verificalas"},
        )
def salir_p(request):
        logout(request)
        return  redirect('home')