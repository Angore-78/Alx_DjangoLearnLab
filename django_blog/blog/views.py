from django.shortcuts import render
from django.http import HttpRequest
from .models import Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView

def index(request):
    return render(request,'blog/index.html')


class BlogCreateView(CreateView):
    blog_post=Post.objects.create()
    template_name='post.html'


class BlogListView(ListView,id):
    blog_posts=Post.objects.order_by("published_date",id)
    template_name='list/.html'
    
class BlogUpdateView(UpdateView):
    blog_post=Post.objects.update()
    template_name='edit.html'

class BlogDetailView(DetailView):
    blog_post=Post.objects.all()
    template_name='detail.html'
    

class BlogDeleteView(DeleteView):
    template_name='delete.html'
