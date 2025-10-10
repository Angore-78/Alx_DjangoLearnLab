from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post




class CustomUser(AbstractUser):
    bio=models.TextField()
    profile_picture=models.ImageField()
    followers=models.ManyToManyField(to='CustomUser')
    following=models.ManyToManyField(to='CustomUser')


class Like(models.Model):
    like=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.PROTECT)




                             
