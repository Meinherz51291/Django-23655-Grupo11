from django.db import models

# Create your models here.

class altaCliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre de Cliente")
    email = models.CharField(max_length=255, verbose_name="Mail del Cliente")
    celular = models.CharField(max_length=15, verbose_name="Celular del Cliente")

