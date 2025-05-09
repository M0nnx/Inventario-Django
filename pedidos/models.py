from django.db import models
from usuarios.models import Usuario, Direccion
from producto.models import Producto
# Create your models here.

class MetodoPago(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion = models.TextField()

    class Meta:
        db_table = 'metodopago'
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion_id = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha =models.DateTimeField(null=True, auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=20,choices=ESTADOS,default='pendiente',verbose_name='Estado del pedido')
    metodo_pago_id = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pedido'
    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

class DetallePedido(models.Model):
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Precio Unitario')
    class Meta:
        db_table = 'detallepedido'
    def __str__(self):
        return f"Detalle de pedido {self.pedido.id} - {self.producto.nombre}"