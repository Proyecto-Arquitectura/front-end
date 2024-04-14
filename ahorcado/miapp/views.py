from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Palabra
# Create your views here.
# MVC = Modelo Vista Controlador
#Controlador => Acciones (metodos)
# MVT = Modelo Template Vista
#Vistas => Acciones (metodos)

layout = """
    <h1>Sitio web con Django</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-prueba">Pagina Prueba</a>
        </li>
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""

# def index(request):
#     '''return HttpResponse(layout+"""
#         <h1>Inicio</h1>
#     """)'''
#     return render(request, 'index.html')

def hola_mundo(request):
    '''return HttpResponse(layout+"""
                        <h1>Hola mundo con Django!!</h1>
                        <h3>Soy Josue </h3>
                        """)'''
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')
    
    '''return HttpResponse(layout+"""
        <h1>Pagina de mi web</h1>
        <p>Creado por Josue Meraz</p>
    """)'''

    return render(request, 'pagina.html')

def contacto(request, nombre=""):
    #return HttpResponse(layout+f"<h2>Contacto {nombre}</h2>")
    return render(request, 'contacto.html')

def crear_palabra(request):
    return render(request, 'crear_palabra.html')

def get_palabras(request):
    palabras = list(Palabra.objects.values('id','palabra','pista'))
    data={
        'mensaje':'exito',
        'palabras':palabras
    }
    return JsonResponse(data)

'''
def save_palabra(request):
    if request.method == 'GET':
        work = request.GET['palabra']
        pista = request.GET['pista']

        p=Palabra(
            palabra = work,
            pista = pista
        )

        p.save()

        return HttpResponse("Palabra creada")

    else:
        return HttpResponse("No se ha creado la palabra")
'''


def save_palabra(request):
    if request.method == 'POST':
        work = request.POST['palabra']
        pista = request.POST['pista']

        p=Palabra(
            palabra = work,
            pista = pista
        )

        p.save()

        return HttpResponse("Palabra creada")

    else:
        return HttpResponse("No se ha creado la palabra")
    
def jugar(request):
    return render(request, 'juego.html')

def login(request):
    return render(request, 'user.html')

def index(request):
    return render(request, 'index.html')