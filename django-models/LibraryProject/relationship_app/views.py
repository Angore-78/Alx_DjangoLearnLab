from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.http import HttpResponse


# Create your views here.
def book_list(response):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(response,'relationship_app/list_books.html',context)
                  
class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['books'] = book.book.all()
        return context

            

