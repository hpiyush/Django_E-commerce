# Generated by Django 2.2.5 on 2019-11-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20191103_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='fullname',
            field=models.CharField(blank='True', default='', max_length=25, null='True'),
        ),
    ]
