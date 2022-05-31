from django.db import models

class Clients(models.Model):
    id = models.IntegerField,
    document = models.CharField(max_length=10)
    first_name =  models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email =  models.CharField(max_length=50)
