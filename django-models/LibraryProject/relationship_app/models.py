from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.ForeignKey()
    def __str__(self):
        return self.title
    

class Library(models.Model):
    name=models.CharField(max_length=40)
    book=models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name=models.CharField(max_length=50)
    library=models.OneToOneField(Library)
    def __str__(self):
        return self.name
    
