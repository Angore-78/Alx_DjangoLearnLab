from django.shortcuts import render
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet,generics
from .models import Post,Comment

class PostViewset(generics.ModelViewSet):
    querry_set=Post.objects.filter(author__in=following_users).order_by('created_at')
    following=Post.objects.following.all()
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


