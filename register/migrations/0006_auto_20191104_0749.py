# Generated by Django 2.2.5 on 2019-11-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20191104_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]