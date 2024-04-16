from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100) 
    discription = models.TextField()
    status = models.CharField(max_length=40)