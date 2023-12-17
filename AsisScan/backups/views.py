from django.shortcuts import render
from Datos_Control_Asistencia.models import Fotos

# Create your views here.


def Backups(request):
        CopiasFotos = Fotos.objects.all()
        
        return render(request,"Backups.html", {'CopiasFotos':CopiasFotos})

