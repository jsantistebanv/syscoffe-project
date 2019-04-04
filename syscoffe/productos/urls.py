from django.conf.urls import url
from .views import listado_productos, HomeProductoView, ListadoProducto, DetalleProducto
urlpatterns = [
    url(r'^listado/$', listado_productos, name='listado'),
    url(r'^listado-templateview/$', HomeProductoView.as_view(), name='tamplateview'),
    url(r'^listado-listview/$', ListadoProducto.as_view(), name='listview'),
    url(r'^(?P<pk>[0-9]+)/$', DetalleProducto.as_view(), name='detalle')
]
