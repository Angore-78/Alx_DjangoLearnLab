from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    bio=models.TextField()
    profile_picture=models.ImageField()
    followers=models.ManyToManyField(to='CustomUser')
