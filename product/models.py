from django.db import models

class CategoryProduct(models.Model):
    description = models.TextField(blank=True, max_length=255)

class Invetary(models.Model):
    categoria=models.OneToOneField(CategoryProduct, related_name="Categoria", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time =  models.DateField(auto_now=True)




class Product(models.Model):
    inventario=models.OneToOneField(Invetary, related_name="inventario", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True)
    precio = models.IntegerField()





# Create your models here.
