
from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea

from random import randint

# Create your views here.

def index(request):
    listita = Tarea.objects.all()
    persona= {"nombre":"Marce",
                "edad":33, "hobbies": ["andar en bici","comer", "sacar fotos", "bailar"],
                "lista_tarea": listita,} 
    
    return render(request, 'inicio.html', persona) #retornamos el saludo
def tarea(request):
    return HttpResponse("Hola soy la vista gorda")
#crear la vista/funcion tarea y conectar con la direccion
#/tarea en el archivo urls.py
#despues ir al navegador y abrir http:........./tareas
def tarea(request):
    return HttpResponse("hola terricolas soy la vista gorda")
def respuesta(request):
    numero= str(randint(500,999))
    print("hola!!!!!!", numero)
    return HttpResponse("hola no se que hice")
def aleatorio(request):
    numero = srt(randibt(1,999))
    respuesta="el numero ganador es"
