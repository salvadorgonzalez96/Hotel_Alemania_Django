# Generated by Django 4.1.7 on 2023-03-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHotel', '0003_cliente_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente_contacto',
            field=models.ManyToManyField(blank=True, to='appHotel.cliente'),
        ),
    ]
