# Generated by Django 4.0.4 on 2022-05-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_residente_name_alter_residente_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
