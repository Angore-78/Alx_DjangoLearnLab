from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} published on {self.published_date.date}"

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    sign_up_date=models.DateTimeField(auto_created=True)
    
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return f"{self.username}, you have successfully loged in."
