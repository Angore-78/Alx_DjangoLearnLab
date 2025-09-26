from rest_framework import serializers
from .models import Author,Book
from django.utils import timezone
#Modelserializer for Book model,inherits from serializers.ModelSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ['id','title','author','publication year']
    
    def validate(self,publication_year):
        if publication_year >timezone.now:
            raise serializers.ValidationError("A book's publication date can't be a time beyond now.")
        return publication_year


#Modelserializer for Author model,inherits from serializers.ModelSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name',]
