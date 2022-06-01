from django.db import models

class Client(models.Model):
    number_document = models.IntegerField()
    first_name =  models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email =  models.CharField(max_length=50)
