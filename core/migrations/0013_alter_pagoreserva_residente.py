# Generated by Django 4.0.4 on 2022-05-19 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_espacio_reservado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoreserva',
            name='residente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.residente'),
        ),
    ]
