from django.db import models

# Create your models here.
class Author(models.Models):
    name=models.CharField(max_length=50)

class Book(models.Models):
    title=models.CharField(max_length=30)
    author=models.ForeignKey()

class Library(models.Models):
    name=models.CharField(max_length=40)
    book=models.ManyToManyField(Book)

class Librarian(models.Models):
    name=models.CharField(max_length=50)
    library=models.OneToOneField(Library)
    
