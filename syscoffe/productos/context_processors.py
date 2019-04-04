from .models import Producto

def promocion_producto(request):
    return {"promocion": Producto.objects.all().first()}