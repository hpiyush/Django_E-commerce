# Generated by Django 2.2.7 on 2019-11-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
