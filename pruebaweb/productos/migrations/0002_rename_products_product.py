# Generated by Django 4.0.4 on 2022-06-01 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_bill_rename_bills_products_bill_product_delete_bills_and_more'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]