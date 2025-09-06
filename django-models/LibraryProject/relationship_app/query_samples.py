from django.shortcuts import render
from .models import Author,Book,Library,Librarian

def book_list(request):
    books = Book.objects.all()
    author = books.author()
    

