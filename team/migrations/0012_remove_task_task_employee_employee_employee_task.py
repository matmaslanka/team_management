# Generated by Django 5.0.2 on 2024-03-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_remove_employee_employee_task_task_task_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_task',
            field=models.ManyToManyField(to='team.task'),
        ),
    ]
