# Generated by Django 2.2.7 on 2019-11-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem_is_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.CharField(default='user', max_length=21),
        ),
    ]
