# Generated by Django 4.0.4 on 2022-05-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_cantreserva_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantreserva',
            name='cantidad',
            field=models.IntegerField(blank=True, default=1, editable=False, null=True),
        ),
    ]
