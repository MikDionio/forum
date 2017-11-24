from django.db import models

# Create your models here.
class User(models.Model):#Question table
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
