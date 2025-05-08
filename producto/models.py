from django.db import models

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
    descripcion = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True,null=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre
