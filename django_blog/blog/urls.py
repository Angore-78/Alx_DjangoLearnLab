from django.urls import path
from . import views

app_name = 'blog'

url_patterns=[
    path('post/',views.BlogListView.as_view(),name='blog'),
    path('post/<int:pk>/delete',views.Delete.as_view(),name='delete'),
    path('post/<int:pk>/update/',views.UpdateView.as_view,name='update'),
    path('post/new/',views.BlogCreateView.as_view,name='post')
]