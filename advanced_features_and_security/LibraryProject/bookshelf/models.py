from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()

    def __str__(self):
        return f'{self.title} by {self.author}'
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField()
    profile_photo = models.ImageField()
   
classmodels.CustomUserManager(BaseUserManager): 
    def create_user(self,date_of_birth,profile_photo):
        CustomUser.objects.create(date_of_birth=date_of_birth,profile_photo=profile_photo )
    def create_superuser(self,date_of_birth,profile_photo):
        CustomUser.objects.create_superuser(date_of_birth=date_of_birth,profile_photo=profile_photo )