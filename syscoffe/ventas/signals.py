from django.db.models import Count, Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import VentaProducto, Venta
from almacenes.models import AlmacenProducto


@receiver([post_save, post_delete], sender=VentaProducto)
def detalle_venta(sender, instance, **kwargs):
    producto = instance.producto
    venta = instance.venta
    # resumen de Ventas
    resultado = VentaProducto.objects.filter(venta=venta).aggregate(
        total=Sum('producto__precio'),
        cantidad=Count('id')
    )
    venta.precio_total = resultado['total']
    venta.total_productos = resultado['cantidad']
    venta.save()

    # descontar stock
    almacen_producto = AlmacenProducto.objects.filter(producto=producto).first()
    if almacen_producto is not None:
        almacen_producto.stock = almacen_producto.stock - instance.cantidad
        almacen_producto.save()

