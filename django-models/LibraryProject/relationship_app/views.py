from django.shortcuts import render
from .models import Book,Library
from django.http import HttpResponse
from django.views.generic import DetailView

# Create your views here.
def book_list(response):
    books = Book.objects.get(title='',author='')
    context = {'book_list':books}
    return render(response,'relationship_app/list_books.html',context)
                  
class LibraryDetailView(DetailView):
    model=Library
    template_name='Library/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['books'] = book.book.all()
        return context

            

