# Generated by Django 2.2.5 on 2019-12-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20191230_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]