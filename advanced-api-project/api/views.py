from django.shortcuts import render
from rest_framework import filters
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics 
from .serializers import BookSerializer



class CreateView(generics.CreateAPIView,IsAuthenticatedOrReadOnly):
    querry_set = Book.objects.all()
    serializer = BookSerializer


    
    
    
class ListView(generics.ListAPIView,IsAuthenticated):
    querry_set = Book.objects.all()
    serializer = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','publication_year','author']

    

class DetailView(generics.RetrieveAPIView,IsAuthenticatedOrReadOnly):
    querry_set = Book.objects.all()
    serializer = BookSerializer

class UpdateView(generics.UpdateAPIView,IsAuthenticatedOrReadOnly):
    querry_set = Book.objects.all()
    serializer = BookSerializer

class DeleteView(generics.DestroyAPIView,IsAuthenticatedOrReadOnly):
    querry_set = Book.objects.all()
    serializer = BookSerializer


    

# Create your views here.
