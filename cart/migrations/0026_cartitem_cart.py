# Generated by Django 2.2.7 on 2019-12-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0025_remove_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='cart.Order'),
        ),
    ]
