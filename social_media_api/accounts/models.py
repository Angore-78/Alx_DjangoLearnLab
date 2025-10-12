from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post




class CustomUser(AbstractUser):
    bio=models.TextField()
    profile_picture=models.ImageField()
    followers=models.ManyToManyField('self',symmetrical=False,related_name='following',)
    following=models.ManyToManyField('self',related_name='followers')
    groups=models.ManyToManyField('auth.Group',
                                  related_name='custom_user_set',)
    user_permissions=models.ManyToManyField('auth.Permission',
                                            related_name='custom_user_permissions_set')
    
    def __str__(self):
        return self.username







                             
