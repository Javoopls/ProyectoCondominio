# Generated by Django 4.0.4 on 2022-05-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_pagoreserva_residente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagoreserva',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
