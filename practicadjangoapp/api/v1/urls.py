from django.urls import path
from rest_framework import routers
from api.v1.tienda.views import ProductoViewSet, CategoriaViewSet, TiendaViewSet

router = routers.SimpleRouter()
router.register(r'productos', ProductoViewSet, basename="productos")
router.register(r'categorias', CategoriaViewSet, basename="categoria")
router.register(r'tiendas', TiendaViewSet, basename="tienda")

urlpatterns = router.urls