from django.db import models

# Create your models here.
TASK_STATUS = (
    ('Not started', 'NOT STARTED'),
    ('In progress', 'IN PROGRESS'),
    ('Finished', 'FINISHED')
)


class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField(default='--')
    task_status = models.CharField(max_length=12, choices=TASK_STATUS, default='Not started')
    # task_deadline

    def __str__(self):
        return f"{self.task_title}"


class Employee(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_description = models.TextField()
    position = models.CharField(max_length=50)
    employee_task = models.ManyToManyField(Task)

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"
