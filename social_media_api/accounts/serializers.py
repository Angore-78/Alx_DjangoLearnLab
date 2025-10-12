from rest_framework import serializers
from .models import CustomUser,Like
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=['id','username','email','bio']
        extra_kwargs={'password':{'write_only':True}}

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    token=serializers.CharField(read_only=True)

    def custom_validation(self,data):
        username=data.get('username')
        password=data.get('password')

        if username and password:
            user=authenticate(response=self.context.get('request'),
                                   username=username,password=password)
            
            if not user:
                raise serializers.ValidationError('Invalid credentials.')
            
            else:
                raise serializers.ValidationError('Must include username and password.')
            
        data['user']=user
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        #Avoid including sensitive fields eg. Passwords
        fields=['username','email','bio','profile_picture','followers','following']
        read_only_fields=['followers','following']


class LikeSerializer(serializers.Serializer):
    class Meta:
        model=Like
        field=['like','user']