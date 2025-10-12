from django.shortcuts import render
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet,generics
from .models import Post,Comment

class PostViewset(generics.ModelViewSet):
    querry_set=Post.objects.all()
    order=querry_set.order_by('created_at')
    serializer=PostSerializer
    permissions=[
        permissions.IsAuthenticatedOrReadOnly 
    ]


class CommentsViewSet(ModelViewSet):
    querry_set=Comment.objects.all()
    serializer=CommentSerializer
    permissions=[
        permissions.IsAuthenticated
    ]


