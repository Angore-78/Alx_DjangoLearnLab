from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView


class BlogCreateView(CreateView):
    blog_post=Post.objects.create()
    template_name='new_post.html'


class BlogListView(ListView,id):
    blog_posts=Post.objects.order_by("published_date",id)
    template_name='blog/blog.html'
    
class BlogUpdateView(UpdateView):
    blog_post=Post.objects.update()
    template_name='edit.html'

class BlogDetailView(DetailView):
    blog_post=Post.objects.all()
    template_name='detail.html'
