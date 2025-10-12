from django.shortcuts import render
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet,generics
from .models import Post,Comment

class PostViewset(generics.GenericAPIView):
    querry_set=Post.objects.order_by('pub_date')
    serializer=PostSerializer
    permissions=[
        permissions.IsAuthenticatedOrReadOnly 
    ]


class CommentsViewSet(ModelViewSet):
    querry_set=Comment
    serializer=CommentSerializer


