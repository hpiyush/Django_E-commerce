# Generated by Django 2.2.7 on 2019-12-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191123_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='untitled', max_length=50),
        ),
    ]
