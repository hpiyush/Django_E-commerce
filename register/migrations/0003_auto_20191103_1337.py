# Generated by Django 2.2.5 on 2019-11-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20191103_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='fullname',
            field=models.CharField(max_length=25),
        ),
    ]
