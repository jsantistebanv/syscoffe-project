from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('get_imagen', 'nombre', 'categoria', 'es_activo')
    list_filter = ('categoria',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creado', 'fecha_modificado')

    def get_imagen(self, obj):
        url = obj.imagen.url if obj.imagen else ''
        return '<img src="{}" width="60px" height="auto">'.format(url)

    get_imagen.allow_tags = True
    get_imagen.short_description = 'Imagen'


