from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio=models.TextField()
    profile_picture=models.ImageField()
    followers=models.ManyToManyField(to='CustomUser')


class Post(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.TextField()
    content=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(Post.author,on_delete=models.CASCADE)
    
                             
