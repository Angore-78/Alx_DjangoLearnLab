from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer,LoginSerializer
from .models import CustomUser
from rest_framework import generics

def login(request):
    pass


def register(request):
    pass


def profile(request):
    pass