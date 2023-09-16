from django.shortcuts import  render

def index(request):
        return render(request, 'index.html')

def login(request):
        return render(request,"login_main.html")

def control(request):
        return render(request,"control.html")