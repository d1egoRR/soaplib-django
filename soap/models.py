from __future__ import unicode_literals

from django.db import models


CHOICES_TIPO_EMISION = (('P', 'Publicidad'), ('C', 'Contenido'))
CHOICES_TIPO_ORIGEN = (('P', 'Publicidad'), ('C', 'Contenido'), ('F', 'Fuente'))


class Origen(models.Model):
    tipo = models.CharField(max_length=1, choices=CHOICES_TIPO_ORIGEN,
                            default="F")

    def __str__(self):
        return self.tipo


class Anunciante(models.Model):
    nombre = models.CharField(max_length=150, unique=True, )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=120, db_index=True)

    def __str__(self):
        return self.nombre


class TipoPublicidad(models.Model):
    # nombre debe ser el id de AdTrack
    nombre = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    es_publicidad = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipo de publicidad"
        ordering = ["nombre"]


class Emision(models.Model):
    tipo = models.CharField(max_length=1, choices=CHOICES_TIPO_EMISION,
                            default="P")

    migracion = models.IntegerField(null=True, blank=True, default=0)

    producto = models.ForeignKey(Producto, null=True)

    fecha = models.DateField(db_index=True, default='1900-01-01')
    hora = models.TimeField(default="00:00")

    orden = models.IntegerField(verbose_name="Numero de Pagina", null=True,
                                blank=True, default=0)

    duracion = models.IntegerField(null=True, blank=True, default=0)

    valor = models.IntegerField(verbose_name="Tarifa", default=0)

    origen = models.CharField(max_length=200, blank=True, db_index=True)
        #Grafica: Imagen (pdf); TV: video

    titulo = models.CharField(verbose_name="Titulo", max_length=255,
                              blank=True)  # se usa para contenido

    observaciones = models.CharField(max_length=500, blank=True, null=True)
    usuario = models.IntegerField(null=True, blank=True, default=0)
    horario = models.IntegerField(null=True, blank=True, default=0)
    tipo_publicidad = models.ForeignKey(TipoPublicidad, null=True, blank=True)
    anunciantes = models.ForeignKey(Anunciante)
    fuente = models.ForeignKey(Origen, null=True, blank=True)
    archivo = models.CharField(max_length=200, null=True, blank=True)
    codigo_directv = models.CharField(max_length=30, null=True, blank=True)
    confirmado = models.BooleanField(default=True)