from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen_url = models.URLField(blank=True,null=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)
   
    class Meta:
        db_table = 'categoria'
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=1)
    stock = models.IntegerField()
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True,null=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'producto'
    def __str__(self):
        return self.nombre

class Valoracion(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'valoraciones'
        unique_together = ('producto_id', 'usuario_id')
