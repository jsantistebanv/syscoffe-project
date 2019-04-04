from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria
# Create your views here.


def listado_productos(request):
    context = {"productos": Producto.objects.all()}
    return render(request, 'productos.html', context=context)


class HomeProductoView(TemplateView):
    template_name = 'productos/listado_completo.html'

    def get_context_data(self, **kwargs):
        context = super(HomeProductoView, self).get_context_data(**kwargs)
        context["titulo"] = "LISTADO COMPLETO"
        context["productos"] = Producto.objects.all()
        context["categorias"] = Categoria.objects.all()
        context["banner"] = "<h4>Producto destacado: {}</h4>".format(Producto.objects.first().nombre)
        return context


class ListadoProducto(ListView):
    model = Producto
    template_name = 'productos/listado.html'
    context_object_name = 'productos'
    paginate_by = 1


class DetalleProducto(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
