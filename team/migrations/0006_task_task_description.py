# Generated by Django 5.0.2 on 2024-03-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_remove_employee_task_employee_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(default='--'),
        ),
    ]