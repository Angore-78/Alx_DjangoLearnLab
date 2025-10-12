from rest_framework import serializers
from .models import CustomUser,Like
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=200 , write_only=True)

    class Meta:
        model=CustomUser
        fields=['id','username','email','bio']
        extra_kwargs={'password':{'write_only':True}}

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    token=serializers.CharField(read_only=True)
        


class LikeSerializer(serializers.Serializer):
    class Meta:
        model=Like
        field=['like','user']