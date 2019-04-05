from django.db import models


class Proveedor(models.Model):
    ruc = models.CharField(max_length=11, db_column='RUC', primary_key=True)
    razon_social = models.CharField(db_column='RAZON_SOCIAL', max_length=11, blank=True, null=True)
    categoria = models.TextField(db_column='CATEGORIA', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROVEEDOR'

