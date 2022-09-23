from django.db import models

# Create your models here.

class Tienda(models.Model):
    """
    Tienda modelo, para Empresa u Supermercado
    """

    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    estado = models.BooleanField(blank=False, help_text="El estado sirve para mostrar si la tienda esta abierta o cerrada")
    imagen_tienda = models.ImageField(upload_to='photos/tienda/local', verbose_name="Imagen Tienda")

    def __str__(self):
        return "{}".format(self.nombre)


class Categoria(models.Model):
    """
    Categoria modelo, Clasificación de los diferentes productos.
    """

    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name="categorias")

    def __str__(self):
        return "{}-{}".format(self.nombre, self.tienda)


class Producto(models.Model):
    """
    Contiene los datos de un producto que se manejan dentro de un negocio
    """

    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio", default=0.0)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad", default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    imagen_producto = models.ImageField(upload_to='photos/tienda/producto', verbose_name="Imagen Producto")

    def __str__(self):
        return "{} Price: {}".format(self.nombre, self.precio)
