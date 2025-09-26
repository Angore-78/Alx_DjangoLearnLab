from django.shortcuts import render
from .models import Book
from django.contrib.auth.models import Permission
from rest_framework import generics 
from .serializers import BookSerializer, AuthorSerializer



class CreateView(generics.CreateView):
    querry_set = Book.objects.all()
    serializer = BookSerializer
    
    
class ListView(generics.ListAPIView):
    querry_set = Book.objects.all()
    serializer = BookSerializer

class DetailView(generics.RetrieveAPIView):
    querry_set = Book.objects.all()
    serializer = BookSerializer

class UpdateView(generics.UpdateAPIView):
    querry_set = Book.objects.all()
    serializer = BookSerializer

class DeleteView(generics.DestroyAPIView):
    querry_set = Book.objects.all()
    serializer = BookSerializer


    

# Create your views here.
