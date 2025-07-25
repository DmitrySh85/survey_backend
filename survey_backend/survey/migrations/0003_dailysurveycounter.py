# Generated by Django 5.1.2 on 2024-11-25 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_tg_id'),
        ('survey', '0002_question_valid_answer_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySurveyCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='employees.employee')),
            ],
            options={
                'verbose_name': 'Счетчик заданий',
                'verbose_name_plural': 'Счетчики заданий',
            },
        ),
    ]
