from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pais(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    valor = models.CharField(max_length=5)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    pais = models.ForeignKey(Pais)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Provincias"