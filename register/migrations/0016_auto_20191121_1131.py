# Generated by Django 2.2.7 on 2019-11-21 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_auto_20191121_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='product',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='quantity',
        ),
    ]
