from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.views.generic import CreateView,TemplateView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import permission_required


class SignUpView(CreateView):
    form = UserCreationForm()
    template_name = 'relationship_app/register.html'


def register(request):
    return HttpResponse('register.html') 

class LoginView(TemplateView):
    template_name = 'login.html'

class LogoutView(TemplateView):
    template_name = 'logout.html'



# Create your views here.
def list_books(response):
    books = Book.objects.all()
    context = {'book_list':books}
    return HttpResponse('relationship_app/list_books.html')

def add_book(request):
    permission_allowed= request.user.has_perm('relationship_app.can_add_book')
    return HttpResponse('add_book.html')

def edit_book(request):
    permission_allowed=request.user.has_perm('relationship_app.can_change_book')
    return HttpResponse('edit_book.html')

def delete_book(request):
    permission_allowed=request.user.has_perm('relationship_app.can_delete_book')
    return HttpResponse('delete_book.html')
                  
class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['books'] = book.book.all()
        return context
    

    

            

