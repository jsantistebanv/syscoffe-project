from django.db import models
from productos.models import Producto
from django.utils.translation import ugettext_lazy as _


class Almacen(models.Model):
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('container')
        verbose_name_plural = _('containers')

    def __str__(self):
        return self.direccion


class AlmacenProducto(models.Model):
    id = models.AutoField(primary_key=True)
    almacen = models.ForeignKey(Almacen)
    producto = models.ForeignKey(Producto)
    stock = models.IntegerField()

    class Meta:
        unique_together = (('almacen', 'producto'),)

    def __str__(self):
        return '{} - {}'.format(self.almacen.direccion, self.producto.nombre)
