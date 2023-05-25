from django.db import models

# Create your models here.

class Employee(models.Model):
    Fullname = models.CharField(max_length=50)
    Department = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=10)
    Email = models.CharField(max_length=100)

