from django.shortcuts import render
from .models import Author,Book,Library,Librarian

def book_list(request):
    books = Book.objects.all()
    author = books.author()

def library_catalogue(request):
    library_name=Library.objects.get(name=library_name)
    available_books=library_name.book.all()

def specific_librarian(request):
    librarian_name = Librarian.objects.get(name=librarian_name)
    library_posted = librarian_name.library() 
    

