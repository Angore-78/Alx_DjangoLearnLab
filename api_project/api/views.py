from django.shortcuts import render
from .models import Book
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .serializers import BookSerializer 

# Create your views here.
class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    add_book = Book.objects.create()
    read_book = Book.object.get(title='')
    def __str__(self):
        return self.add_book(),self.read_book()

