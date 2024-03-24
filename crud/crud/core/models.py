from django.db import models


# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length = 100)
    Position = models.CharField(max_length=25)
    Phone = models.CharField(max_length= 10)