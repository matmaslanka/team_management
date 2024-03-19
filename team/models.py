from django.db import models

# Create your models here.

class Team(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_description = models.TextField()
    position = models.CharField(max_length=50)