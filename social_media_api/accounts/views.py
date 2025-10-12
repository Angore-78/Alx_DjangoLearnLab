from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer,LoginSerializer,UserProfileSerializer
from .models import CustomUser
from rest_framework import generics

class RegistrationView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserRegistrationSerializer

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        user=serializer.save()
        token,created=Token.objects.get_or_create(user=user)

        return Response({})


def register(request):
    pass


def profile(request):
    pass