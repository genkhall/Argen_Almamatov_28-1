# Generated by Django 4.2.1 on 2023-05-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
