from django.shortcuts import render
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Post,Comment

class PostViewset(ModelViewSet):
    querry_set=Post
    serializer=PostSerializer
    permissions=[
        permissions.IsAuthenticatedOrReadOnly 
    ]


class CommentsViewSet(ModelViewSet):
    querry_set=Comment
    serializer=CommentSerializer


