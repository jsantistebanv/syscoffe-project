from django.contrib import admin
from .models import Venta, VentaProducto


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    pass


@admin.register(VentaProducto)
class VentaProductoAdmin(admin.ModelAdmin):
    pass
