from django.contrib import admin
from .models import Bill, Bill_product

# Register your models here.

admin.site.register(Bill)
admin.site.register(Bill_product)