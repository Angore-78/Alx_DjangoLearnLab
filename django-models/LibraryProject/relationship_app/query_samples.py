from django.shortcuts import render
from relationship_app.models import Book,Library,Librarian,Author

def book_list(request):
    books = Book.objects.all()
    books.all()
    author_name=Author.objects.get(name=author_name)
    author=Author.objects.filter(author=author)

def library_catalogue(request):
    library_name=Library.objects.get(name=library_name)
    library_name.book.all()

def specific_librarian(request):
    librarian_library= Librarian.objects.get(library='')
    librarian_library.library() 
    

