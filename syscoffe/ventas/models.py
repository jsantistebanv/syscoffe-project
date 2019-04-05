from django.db import models


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.FloatField(blank=True, null=True, default=None)
    total_productos = models.PositiveIntegerField(blank=True, null=True, default=None)
    inpuesto = models.FloatField(blank=True, null=True, default=None)

    def __str__(self):
        return 'venta: {}'.format(self.id)


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta)
    producto = models.ForeignKey('productos.Producto')
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return 'venta {} - {}'.format(self.venta_id, self.producto.nombre)
