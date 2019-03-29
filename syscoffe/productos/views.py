from django.shortcuts import render
from .models import Producto
# Create your views here.


def listado_productos(request):
    context = {"productos": Producto.objects.all()}
    return render(request, 'productos.html', context=context)
