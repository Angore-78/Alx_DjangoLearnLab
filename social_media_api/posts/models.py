from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser as user

class Post(models.Model):
    author=models.ForeignKey(user,on_delete=models.CASCADE)
    title=models.TextField()
    content=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    commenter=models.ForeignKey(User,on_delete=models.CASCADE)


