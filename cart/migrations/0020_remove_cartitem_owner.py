# Generated by Django 2.2.7 on 2019-12-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0019_auto_20191210_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='owner',
        ),
    ]
