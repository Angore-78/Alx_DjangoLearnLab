from rest_framework import serializers
from .models import Author,Book

#Modelserializer for Book model,inherits from serializers.ModelSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['id','title','author',]

#Modelserializer for Author model,inherits from serializers.ModelSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name',]
