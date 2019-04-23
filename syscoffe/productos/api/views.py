from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from ..models import Categoria, Producto
from .serializers import CategoriaSerializer

class CategoriaApiView(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class CategoriaDosApiView(ViewSet):
    def list(self, ):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data)