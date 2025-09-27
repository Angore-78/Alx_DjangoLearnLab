from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView



url_patterns = [
    path('api/books/',ListView.as_view(),name = 'books'),
    path('api/books/<int:pk>/', DetailView.as_view(), name = 'detail'),
    path('api/books/create/', CreateView.as_view(), name = 'create'),
    path('api/books/update/', UpdateView.as_view(), name = 'update' ),
    path('api/books/delete/', DeleteView.as_view(),name = 'delete')
]

