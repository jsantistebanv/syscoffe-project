from django.conf.urls import url
from .views import listado_productos, HomeProductoView, ListadoProducto
urlpatterns = [
    url(r'^listado/$', listado_productos, name='listado'),
    url(r'^listado-templateview/$', HomeProductoView.as_view(), name='tamplateview'),
    url(r'^listado-listview/$', ListadoProducto.as_view(), name='listview')
]
