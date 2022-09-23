import os
from django.contrib import admin
from tienda.models import Categoria, Producto, Tienda

# Register your models here.
class TiendaAdmin(admin.ModelAdmin):
    """
    Tienda Admin
    """
    list_display = ("nombre", "direccion", "estado", "imagen_tienda")
    search_fields = ("nombre", "direccion", "estado")
    list_filter = ("nombre", "direccion", "estado")
    fieldsets = ((("Información de Cuenta"), {"fields": ("nombre", "direccion", "estado", "imagen_tienda")}),)

class CategoriaAdmin(admin.ModelAdmin):
    """
    Categoria Admin
    """

    list_display = ("nombre", "descripcion", "tienda")
    search_fields = ("nombre", "descripcion", "tienda")
    list_filter = ("nombre", "descripcion", "tienda")
    fieldsets = ((("Datos Básicos"), {"fields": ("tienda", "nombre", "descripcion")}),)


class ProductAdmin(admin.ModelAdmin):
    """
    Admin Product
    """

    list_display = ("nombre", "cantidad", "precio", "categoria", "descripcion","imagen_producto")
    search_fields = ("nombre", "descripcion", "categoria")
    list_filter = ("nombre", "descripcion", "categoria")
    fieldsets = (
        (
            ("Datos Básicos"),
            {
                "fields": (
                    "categoria",
                    "nombre",
                    "cantidad",
                    "precio",
                    "descripcion",
                    "imagen_producto",
                )
            },
        ),
    )
admin.site.register(Tienda, TiendaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductAdmin)
