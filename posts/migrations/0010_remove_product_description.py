# Generated by Django 4.2.1 on 2023-05-20 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_product_description_alter_product_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]