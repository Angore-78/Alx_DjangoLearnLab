from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DeleteView,DetailView


class BlogListView(ListView):
    blog_posts=Post.objects.order_by("published_date")
    template_name='blog/blog.html'
    