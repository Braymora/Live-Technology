from django.db import models

# Create your models here.
class Cursos(models.Model):
    id_curso = models.TextField(max_length=15)  # Campo de clave primaria
    nombre = models.CharField(max_length=255)  # Campo de texto para el nombre
    descripcion = models.TextField()  # Campo de texto para la descripción
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo decimal para el precio
 # Para representar el curso por su nombre
