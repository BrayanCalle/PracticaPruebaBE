from rest_framework import serializers
from tienda.models import Tienda, Categoria, Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        read_only_fields = [
            "id",
        ]
        fields = [
            "created_at", "nombre", "descripcion", "precio",
            "cantidad", "categoria", "imagen_producto"
        ] + read_only_fields
        depth = 2


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        read_only_fields = [
            "id",
        ]
        fields = [
            "nombre","descripcion","tienda"
        ] + read_only_fields


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        read_only_fields = [
            "id",
        ]
        fields = [
            "nombre", "direccion", "estado", "imagen_tienda"
        ] + read_only_fields
