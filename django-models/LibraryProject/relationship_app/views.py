from django.shortcuts import render
from .models import Book,Library
from django.views.generic import DetailView

# Create your views here.
def book_context_list(request):
    book = Book.object.all()
    book_display = {'catalogue':f'{book.title()} by {book.author()}'}
    return render(request,'book/catalogue.html',book_display)

class LibraryDetailview(DetailView):
    model = Library
    template_name = 'library/library_detail.html'

    def library_catalogue(self):
        availed_books = self.object.book.all()
        

