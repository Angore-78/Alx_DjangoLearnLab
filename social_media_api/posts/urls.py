from django.urls import path
from rest_framework import routers
from . import views

app_name='posts'

router=routers.DefaultRouter()
router.register(r'posts',views.PostViewset,basename='post')
router.register(r'comments',views.CommentsViewSet,basename='comment')
