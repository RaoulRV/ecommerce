# Generated by Django 3.2 on 2022-12-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20221113_1211'),
        ('products', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Carlist',
        ),
    ]
