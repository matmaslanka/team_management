# Generated by Django 5.0.2 on 2024-03-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_rename_task_employee_employee_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('not_started', 'NOT STARTED'), ('in_progress', 'IN PROGRESS'), ('finished', 'FINISHED')], default='not_started', max_length=12),
        ),
    ]
