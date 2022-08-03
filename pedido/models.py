from django.db import models
from account.models import Provider
from product.models import Product
# Create your models here.
class Order(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    ordernumber = models.IntegerField()
    orderdate = models.DateTimeField(auto_now_add=True)
    senddate = models.DateTimeField(auto_now=True)


class Detalle(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filedetalle = models.FileField()
    cantidad = models.IntegerField(default=1)
    monto = models.IntegerField()
