from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth.views import  LoginView ,LogoutView

urlpatterns = [
    path('books/',views.list_books,name='list_books'),
    path('library/',views.LibraryDetailView.as_view(),name='library'),
    path('signup/', views.SignUpView.as_view(),name = 'signup'),
    path('login/', LoginView.as_view(),name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    ]
    


