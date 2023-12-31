"""
URL configuration for AsisScan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register.views import index
from AsisScan.view import login
from esp_task.views import control
from AsisScan.view import configuraciones
from AsisScan.view import home
from register.views import salir_p
from esp_task.views import video_imagen1
from esp_task.views import video_imagen2
from esp_task.views import obtener_imagen
from esp_task.views import obtener_imagen2
from esp_task.views import actualizar_movimiento
from Datos_Control_Asistencia.views import control_asistencia
from backups.views import Backups
from AsisScan.view import UserProfile

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index,),
    path('', home, name='home'), 
    path('login/', login),
    path('control/',control, name='control'),
    path('configuraciones/',configuraciones),
    path('video_imagen1/',video_imagen1,name='video_imagen'),
    path('salir_p/',salir_p,name='salir_p'),
    path('video_imagen2/',video_imagen2,name='video_imagen2'),
    path('obtener_imagen/',obtener_imagen),
    path('obtener_imagen2/',obtener_imagen2),
    path('backups/',Backups),
    path('actualizar_movimiento/<str:direccion>/', actualizar_movimiento, name='actualizar_movimiento'),
    path('UserProfile/',UserProfile),
    path('control_asistencia/',control_asistencia)
]
   

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)