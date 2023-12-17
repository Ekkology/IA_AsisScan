from django.shortcuts import render
from .models import Administrativos, Docentes, Estudiantes
from .models import Fotos
from .models import Facultad
from .models import persona
# Create your views here.

def control_asistencia(request):
    administrativos = Administrativos.objects.all()
    docentes = Docentes.objects.all()
    estudiantes = persona.objects.all() 
    facultad = Facultad.objects.all()
    fotos = Fotos.objects.get(id_foto=15)
    foto_64 = fotos.foto
    #if 'base64,' in foto_64:
    #foto_64 = foto_64.split('base64,')[1]

    return render(
       request,
        "control_asistencia.html",
        {"administrativos": administrativos, "docentes": docentes, "estudiantes": estudiantes, "fotoss": foto_64, "facultad": facultad}
    )
