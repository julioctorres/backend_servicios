from django.db import models

class Product(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    attribute_4 = models.CharField(max_length=40)



