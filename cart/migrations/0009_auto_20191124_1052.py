# Generated by Django 2.2.7 on 2019-11-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20191123_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]