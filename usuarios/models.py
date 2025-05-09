from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    class Meta:
        db_table = 'usuario'
    def __str__(self):
        return self.username
    
class Direccion(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.BigIntegerField(null=True, blank=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=255,blank=True, null=True)
    es_default = models.BooleanField(default=False)
    class Meta:
        db_table = 'direccion'
    def __str__(self):
        return f"{self.direccion},{self.ciudad},{self.pais}"
