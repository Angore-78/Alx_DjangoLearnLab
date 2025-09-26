from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView



url_patterns = [
    path('api/books/',ListView.as_view(),name = 'books'),
    path('api/books/<int:pk>/', DetailView.as_view(), name = 'books/<int:pk>/'),
    path('api/book/create/', CreateView.as_view(), name = 'create'),
    path('api/book/update', UpdateView.as_view(), name = 'update' ),
    path('api/')
]

