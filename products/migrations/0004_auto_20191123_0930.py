# Generated by Django 2.2.7 on 2019-11-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
