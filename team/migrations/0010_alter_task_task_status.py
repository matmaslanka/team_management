# Generated by Django 5.0.2 on 2024-03-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Not started', 'NOT STARTED'), ('In progress', 'IN PROGRESS'), ('Finished', 'FINISHED')], default='Not started', max_length=12),
        ),
    ]
