from django.urls import path
from . import views
from . import views

app_name = 'blog'

url_patterns=[
    path('post/list/',views.BlogListView.as_view(),name='list'),
    path('post/<int:pk>/delete/',views.DeleteView.as_view(),name='delete'),
    path('post/<int:pk>/update/',views.UpdateView.as_view,name='update'),
    path('post/<int:pk>/detail/',views.BlogDetailView.as_view(),name='detail'),
    path('post/new/',views.BlogCreateView.as_view(),name='post')
]