from django.apps import AppConfig


class VentasConfig(AppConfig):
    name = 'ventas'

    def ready(self):
        from ventas.signals import detalle_venta

