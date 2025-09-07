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
    ]
    


