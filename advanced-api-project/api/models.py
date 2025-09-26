from django.db import models

class Author(models.Model):
    name = models.CharField('')


class Book(models.Model):
    title = models.CharField('')
    publication_year = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
