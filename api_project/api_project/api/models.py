from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(50)
    author = models.CharField(50)
    
