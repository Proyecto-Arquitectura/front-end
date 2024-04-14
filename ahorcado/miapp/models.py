from django.db import models

# Create your models here.

class Palabra(models.Model):
    palabra = models.CharField(max_length=50)
    pista = models.CharField(max_length=200)

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
