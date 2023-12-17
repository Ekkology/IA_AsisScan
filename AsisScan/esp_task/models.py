from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings  # Asegúrate de importar la configuración de Django
# Create your models here.






class mi_tabla2(models.Model):
    id = models.AutoField(primary_key=True)
    data_base64 = models.TextField()
    
    class Meta:
        db_table = 'mi_tabla'



class camaras (models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.TextField()
    lugar = models.TextField()
    encendido = models.IntegerField(default=0)

    class Meta:
        db_table = 'dispositivos' 



class movimientoservo(models.Model):
    id = models.AutoField(primary_key=True)
    movimiento =  models.IntegerField()

    class Meta:
        db_table = 'movimientoservo'


class reconocimientoBD(models.Model):
    id = models.AutoField(primary_key=True)
    imagen_reconocida = models.TextField()
    class Meta:
        db_table ='reconocimiento'