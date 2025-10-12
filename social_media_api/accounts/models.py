from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post




class CustomUser(AbstractUser):
    bio=models.TextField()
    profile_picture=models.ImageField()
    followers=models.ManyToManyField('self',symmetrical=False,related_name='following',)
    following=models.ManyToManyField('self',related_name='followers')








                             
