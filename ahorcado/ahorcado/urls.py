"""
URL configuration for ahorcado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Importar app con mis vistas
from miapp import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('get-palabras/', views.get_palabras, name="get_palabras")
    # path('admin/', admin.site.urls),
    # path('', views.jugar, name="jugar"),
    # #path('', views.index, name="index"),
    # path('inicio/', views.index, name="inicio"),
    # path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    # path('pagina-prueba/', views.pagina, name="pagina"),
    # path('pagina-prueba/<int:redirigir>', views.pagina, name="pagina"),
    # path('contacto/', views.contacto, name="contacto"),
    # path('contacto/<str:nombre>', views.contacto, name="contacto"),
    # path('crear-palabra/', views.crear_palabra, name="crear_palabra"),
    # path('save-palabra/', views.save_palabra, name="save_palabra")
]
