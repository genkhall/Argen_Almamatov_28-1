# Generated by Django 4.2.1 on 2023-06-03 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_remove_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='prise',
        ),
    ]
