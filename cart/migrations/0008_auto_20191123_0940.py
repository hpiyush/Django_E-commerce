# Generated by Django 2.2.7 on 2019-11-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20191123_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
