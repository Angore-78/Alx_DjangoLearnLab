from django.urls import path
from .views import BlogListView

app_name = 'blog'

url_patterns=[
    path('post/',BlogListView.as_view(),name='blog'),
    
]