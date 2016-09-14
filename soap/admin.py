from django.contrib import admin

from .models import Pais


class PaisAdmin(admin.ModelAdmin):

    search_fields = ['descripcion', 'valor']
    ordering = ['descripcion']
    list_display = ['descripcion', 'valor']

admin.site.register(Pais, PaisAdmin)