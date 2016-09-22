from django.contrib import admin

from .models import Emision, Origen, Anunciante, Producto, TipoPublicidad


class OrigenAdmin(admin.ModelAdmin):

    search_fields = ['tipo']
    ordering = ['tipo']
    list_display = ['id', 'tipo']


class AnuncianteAdmin(admin.ModelAdmin):

    search_fields = ['nombre']
    ordering = ['nombre']
    list_display = ['id', 'nombre']


class ProductoAdmin(admin.ModelAdmin):

    search_fields = ['nombre']
    ordering = ['nombre']
    list_display = ['id', 'nombre']


class TipoPublicidadAdmin(admin.ModelAdmin):

    search_fields = ['nombre', 'descripcion', 'es_publicidad']
    ordering = ['nombre']
    list_display = ['id', 'nombre', 'descripcion', 'es_publicidad']


class EmisionAdmin(admin.ModelAdmin):

    search_fields = ['tipo', 'migracion', 'producto', 'fecha', 'hora', 'orden',
                    'duracion', 'valor', 'origen', 'titulo', 'observaciones',
                    'usuario', 'horario', 'tipo_publicidad', 'anunciantes',
                    'fuente', 'archivo', 'codigo_directv', 'confirmado']
    ordering = ['tipo']
    list_display = ['id', 'tipo', 'migracion', 'producto', 'fecha', 'hora',
                    'orden', 'duracion', 'valor', 'origen', 'titulo',
                    'observaciones', 'usuario', 'horario', 'tipo_publicidad',
                    'anunciantes', 'fuente', 'archivo', 'codigo_directv',
                    'confirmado']

admin.site.register(Emision, EmisionAdmin)
admin.site.register(Origen, OrigenAdmin)
admin.site.register(Anunciante, AnuncianteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoPublicidad, TipoPublicidadAdmin)

