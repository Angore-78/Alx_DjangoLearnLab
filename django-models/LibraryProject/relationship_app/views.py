from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/register.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class LogoutView(TemplateView):
    template_name = 'logout.html'



# Create your views here.
def list_books(response):
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
    

    

            

