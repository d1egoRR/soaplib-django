from django.contrib import admin

from .models import Pais, Provincia


class PaisAdmin(admin.ModelAdmin):

    search_fields = ['descripcion', 'valor']
    ordering = ['descripcion']
    list_display = ['id', 'descripcion', 'valor']


class ProvinciaAdmin(admin.ModelAdmin):

    search_fields = ['descripcion']
    ordering = ['descripcion']
    list_display = ['id', 'descripcion']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)