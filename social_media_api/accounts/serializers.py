from rest_framework import serializers
from .models import CustomUser,Like

class UserSerializer(serializers.Serializer):
    class Meta:
        model=CustomUser
        fields=['bio','profile','following','followers']

class LikeSerializer(serializers.Serializer):
    class Meta:
        model=Like
        field=['like','user']