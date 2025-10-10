from django.db import models
from django.contrib.auth.models import User


class Notifications(models.Model):
    recepient=models.ForeignKey(User,on_delete=models.CASCADE)
    actor=models.ForeignKey(User,on_delete=models.CASCADE)
    verb=models.CharField(max_length=200)
    target=models.GenericForeignKey
    timestamp=models.DateTimeField(auto_now_add=True)