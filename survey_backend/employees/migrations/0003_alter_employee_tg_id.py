# Generated by Django 5.1.2 on 2024-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='tg_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
