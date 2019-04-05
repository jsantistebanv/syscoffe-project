from django.contrib import admin
from .models import Almacen, AlmacenProducto


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('direccion',)


@admin.register(AlmacenProducto)
class AlmacenProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'almacen', 'producto', 'stock')

