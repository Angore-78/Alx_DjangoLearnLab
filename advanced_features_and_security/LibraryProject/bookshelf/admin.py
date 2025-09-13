from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
