from rest_framework import viewsets
from tienda.models import Tienda, Categoria, Producto
from api.v1.tienda.serializers import ProductoSerializer, CategoriaSerializer, TiendaSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from pagination import ProductoPagination

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class= ProductoSerializer
    pagination_class = ProductoPagination
    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    ordering_fields = ["created_at", "nombre", "precio"]
    ordering = ["-created_at"]
    search_fields = ["nombre", "categoria__nombre", "precio"]
    filterset_fields = {
        'precio': ['gte','lte'],
        'categoria__nombre': ['exact'],
        'categoria__tienda': ['exact'],
        # 'estado__nombre': ['exact'],
    }
    queryset = Producto.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class= CategoriaSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Categoria.objects.all()

class TiendaViewSet(viewsets.ModelViewSet):
    serializer_class= TiendaSerializer
    filter_backends = [OrderingFilter]
    ordering = ["nombre"]
    queryset = Tienda.objects.all()

