from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name='accounts'

urlpatterns=[
    path('/register/',views.RegistrationView.as_view()),
    path('/login/',views.UserLoginView.as_view()),
    path('/profile/',views.UserProfile.as_view()),
]


