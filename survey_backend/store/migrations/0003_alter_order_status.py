# Generated by Django 5.1.2 on 2024-10-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ORDERED', 'Заказан'), ('ISSUED', 'Выдан')], default='ORDERED'),
        ),
    ]
