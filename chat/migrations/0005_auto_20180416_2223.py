# Generated by Django 2.0.4 on 2018-04-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20180416_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
