from django.db import models


#class Meta:
        #managed = False  # Indica a Django que no debe gestionar las migraciones
        #db_table = 'nombre_de_la_tabla_en_tu_base_de_datos'


# Create your models here.
class Administrativos(models.Model):
    Nombre = models.CharField(max_length=255)
    Rol = models.CharField(max_length=255)
    Asistencia = models.CharField(max_length=255)

    def __str__(self):
      return self.Nombre

class Docentes(models.Model):
    Nombre = models.CharField(max_length=255)
    Asistencia = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Nombre
    

class Estudiantes(models.Model):
    Nombre = models.CharField(max_length=255)
    Facultad = models.CharField(max_length=255)
    Carrera = models.CharField(max_length=255)
    Año = models.CharField(max_length=255)
    Grupo = models.CharField(max_length=255)
    Asistencia = models.CharField(max_length=255)

    def __str__(self):
       return self.Nombre


class Fotos(models.Model):
    id_foto = models.AutoField(primary_key=True)
    id_persona = models.IntegerField()
    foto = models.TextField()
    descripcion = models.TextField(null = True)
    class Meta :
        db_table = 'fotos'

class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    facultad = models.TextField()
    descripcion = models.TextField()
    class Meta :
        db_table = 'facultades'

class persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    cedula = models.TextField()
    correo = models.TextField()
    class Meta:
        db_table = 'personas'
    
