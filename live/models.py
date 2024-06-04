from django.db import models

# Create your models here.
class Cursos(models.Model):
    id_curso = models.TextField(max_length=15)  # Campo de clave primaria
    nombre = models.CharField(max_length=255)  # Campo de texto para el nombre
    descripcion = models.TextField()  # Campo de texto para la descripción
    imagen = models.TextField(default='hola')
    precio = models.IntegerField()  # Campo decimal para el precio
 # Para representar el curso por su nombre
