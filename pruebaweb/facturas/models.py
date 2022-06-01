from django.db import models
from cliente.models import Client
from productos.models import Product

class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.IntegerField()
    code = models.IntegerField()

class Bill_product(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
