# Generated by Django 4.2.1 on 2023-05-18 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_product_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.product')),
            ],
        ),
    ]
