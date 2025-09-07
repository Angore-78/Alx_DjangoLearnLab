from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth.views import  LoginView ,LogoutView

urlpatterns = [
    path('books/',views.list_books,name='list_books'),
    path('library/',views.LibraryDetailView.as_view(),name='library'),
    path('register/', views.register,name = 'register'),
    path('login/', LoginView.as_view(template_name=""),name = 'login'),
    path('logout', LogoutView.as_view(template_name=''), name = 'logout'),
    path('Admin/',views.Admin,name = 'Admin'),
    path('librarian/', views.Librarian, name = 'librarian'),
    path('member/', views.Member, name = 'member'),
    path('book_add/',views.book_add,name='book_add'),
    path('book_change/',views.book_change,name='book_change'),
    path('book_delete/',views.book_delete,name='book_delete'),
    ]
    


