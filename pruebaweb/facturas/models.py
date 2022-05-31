from django.db import models
from cliente.models import Clients
from productos.models import Products

class Bills(models.Model):
    id_bills = models.IntegerField
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.IntegerField
    code = models.IntegerField

class Bills_products(models.Model):
    id = models.IntegerField
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
