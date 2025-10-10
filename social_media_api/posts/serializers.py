from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.Serializer):
    class Meta:
        model=Post
        fields=['author','title','content','created_at','updated_at']

class CommentSerializer(serializers.Serializer):
    class Meta:
        model=Comment
        fields=['post','commenter']