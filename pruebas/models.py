from django.db import models

# Create your models here.


class Director(models.Model):
    nombre = models.CharField(
        max_length=50, help_text="Introduce nombre de director")

    def __str__(self):
        return self.nombre


class Peliculas(models.Model):
    nombre = models.CharField(
        max_length=50, help_text="Introduce el título de la película")
    descripcion = models.TextField(
        help_text="Introduce la descripción de la película")
    director = models.ForeignKey(
        "Director", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
