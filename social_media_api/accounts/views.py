from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer,LoginSerializer,UserProfileSerializer
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import generics

class RegistrationView(generics.CreateAPIView):
    queryset=CustomUser.objects.create_user()
    serializer_class=UserRegistrationSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        user=serializer.save()
        token=Token.objects.create(user=user)



class UserProfile(generics.ModelViewSet):
    querry_set=CustomUser.objects.get('profile')
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated]


class UserLoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token=Token.objects.get(user=user)
        created=Token.objects.create(user=user)
        return Response(
            {'token':token.key}
        )