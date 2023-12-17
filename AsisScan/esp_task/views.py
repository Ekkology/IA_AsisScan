import base64
from django.http import JsonResponse
from django.shortcuts import render
from esp_task.models import mi_tabla2
from esp_task.models import reconocimientoBD
from .models import camaras
from .models import movimientoservo
from django.shortcuts import redirect
from threading import Timer
import cv2
import numpy as np
import time
from .forms import CamarasForm
import cv2
import os
import face_recognition
import datetime
import mysql.connector
from io import BytesIO
import base64
from PIL import Image
import numpy as np
import subprocess
from django.http import HttpResponse
from django.conf import settings
import os
valor_anterior = None
from django.http import JsonResponse
import string
import threading





def control(request):
    global valor_anterior
    if request.method == 'POST':
        form = CamarasForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('control')
           
        else:
            return JsonResponse({'error': 'Error en el formulario'})  
        

   
    form = CamarasForm()  

    foto_2 = mi_tabla2.objects.get(id=4)
    if foto_2:
        data_base64_2 = foto_2.data_base64
        if 'base64,' in data_base64_2:
            data_base64_2 = data_base64_2.split('base64,')[1]
       
        if data_base64_2 != valor_anterior:
            
            primera_camara = camaras.objects.get(id=2)
            if primera_camara:
                primera_camara.encendido = 1
                primera_camara.save()
           
            t = Timer(15.0, reset_encendido)
            t.start()
        valor_anterior = data_base64_2

    camarass = camaras.objects.all()
    return render(request, 'control.html', {'camaras': camarass, 'form': form})





def video_imagen1(request):

    return render(request, "video_imagen1.html")

def obtener_imagen(request):
    #se optiene de la primera tabla cuando la imagen aun no esta procesada
    #reconocimiento()
    # Obtener la imagen base64 de la base de datos
    foto = reconocimientoBD.objects.get(id=1)
    if foto:
        data_base64 = foto.imagen_reconocida
        if 'base64,' in data_base64:
            data_base64 = data_base64.split('base64,')[1]

        return JsonResponse({'imagen_base64': data_base64})
    else:
        return JsonResponse({'error': 'No se encontró ninguna imagen en la base de datos'})

#Funcion  para lasegunda imagen 
from threading import Timer

def obtener_imagen2(request):
    global valor_anterior
    foto_2 = mi_tabla2.objects.get(id=1)
    if foto_2:
        data_base64_2 = foto_2.data_base64
        if 'base64,' in data_base64_2:
            data_base64_2 = data_base64_2.split('base64,')[1]
        return JsonResponse({'imagen_base64_2': data_base64_2})
    else:
        return JsonResponse({'error': 'No se encontró ninguna imagen en la base de datos'})
def reset_encendido():
    primera_camara = camaras.objects.get(id=2)
    if primera_camara:
        primera_camara.encendido = 0
        primera_camara.save()

def video_imagen2(request): 
        return render(request,"video_imagen2.html")

def actualizar_movimiento(request, direccion):
    if direccion == 'izquierda':
        movimiento = -1
    elif direccion == 'derecha':
        movimiento = 1
    elif direccion == 'arriba':
        movimiento = 2
    elif direccion == 'abajo':
        movimiento = -2
    else:
        movimiento = 0

    mov = movimientoservo.objects.get(id=1) 
    mov.movimiento = movimiento
    mov.save()

    return JsonResponse({'message': 'Movimiento actualizado con éxito'})




def obtener_imagen_desde_base_datos(image_id=1):
    try:
        imagen_base64 = mi_tabla2.objects.values_list('data_base64', flat=True).filter(id=image_id).first()
        return imagen_base64
    except mi_tabla2.DoesNotExist:
        return None

def update_imagen(base64_img, image_id=1):
    try:
        reconocimiento_obj = reconocimientoBD.objects.get(id=image_id)
        reconocimiento_obj.imagen_reconocida = base64_img
        reconocimiento_obj.save()
    except reconocimientoBD.DoesNotExist:
        print("Error al actualizar la imagen: El objeto no existe.")
def decodificar_base64(base64_str):
    try:
       
        padding = '=' * (4 - len(base64_str) % 4)
        base64_str += padding

        
        if len(base64_str) % 4 != 0:
            print(f"Error: Longitud de cadena base64 no válida. Base64 actual: {base64_str}")
            return None

       
        image_data = base64.b64decode(base64_str)
        image = Image.open(BytesIO(image_data))

        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return None




def cargar_imagenes_desde_carpeta(imageFacesPath):
    facesEncodings = []
    facesNames = []

    for file_name in os.listdir(imageFacesPath):
        image = cv2.imread(os.path.join(imageFacesPath, file_name))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        f_encoding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
        facesEncodings.append(f_encoding)
        facesNames.append(file_name.split(".")[0])

    return facesEncodings, facesNames

def reconocimiento():
    imageFacesPath = os.path.join(settings.MEDIA_ROOT, 'Fotos')
    facesEncodings, facesNames = cargar_imagenes_desde_carpeta(imageFacesPath)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        imagenes_base64 = obtener_imagen_desde_base_datos()

        if imagenes_base64:
            frame = decodificar_base64(imagenes_base64)

            if frame is None:
                print("Error decoding base64 or obtaining frame.")
                continue  
        else:
            print("No se encontraron imágenes en la base de datos.")
            exit()

       
        frame = cv2.flip(frame, 1)
        orig = frame.copy()
        faces = faceClassif.detectMultiScale(frame, 1.1, 5)

        for (x, y, w, h) in faces:
            face = orig[y: y + h, x: x + w]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            actual_face_encoding = face_recognition.face_encodings(face, known_face_locations=[(0, w, h, 0)])[0]
            result = face_recognition.compare_faces(facesEncodings, actual_face_encoding)

            if True in result:
                index = result.index(True)
                name = facesNames[index]
                color = (125, 220, 0)
                print(name)
                hoy = datetime.datetime.utcnow()
                print(hoy)
            else:
                name = "Desconocido"
                color = (50, 50, 255)

            cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)

        _, buffer = cv2.imencode('.jpg', frame)
        base64_img = base64.b64encode(buffer).decode()
        update_imagen(base64_img)

#def reconocimiento_loop():
   # while True:
      #  reconocimiento()

# Inicia el hilo para la función de reconocimiento
#reconocimiento_thread = threading.Thread(target=reconocimiento_loop)
#reconocimiento_thread.start()
