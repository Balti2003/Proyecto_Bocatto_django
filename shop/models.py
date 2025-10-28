from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model): # Categorias de productos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Product(models.Model): # Producto
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre


class Order(models.Model): # Orden de compra hecha por un usuario
    ESTADOS = [
        ('pendiente_pago', 'Pendiente de Pago'),
        ('pagado', 'Pagado'),
        ('en_preparacion', 'En Preparación'),
        ('listo', 'Listo para Entregar'),
        ('en_camino', 'En Camino'),
        ('enviado', 'Enviado / Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    METODOS_PAGO = [
        ("efectivo", "Efectivo"),
        ("transferencia", "Transferencia"),
    ]

    METODOS_ENTREGA = [
        ("retiro", "Retiro en el local"),
        ("delivery", "Delivery"),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente_pago')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO, default="efectivo")
    metodo_entrega = models.CharField(max_length=20, choices=METODOS_ENTREGA, default="retiro")
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario}"


class OrderItem(models.Model): #Esta tabla une prodcutos con el pedido de un usuario, un pedido puede tener muchos productos
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario