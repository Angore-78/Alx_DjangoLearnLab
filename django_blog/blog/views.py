from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .forms import PostForm,CommentForm



def index(response,id):
    blog_p=Post.objects.get(id=id)
    return render(response,'blog/index.html',{'text':blog_p.title})

def post(response):
    form = PostForm
    return render(response,'blog/post.html',{"form":form})

def commentview(response):
    form =CommentForm
    return render(response,'blog/')

class UserLogin(CreateView):
    form = UserCreationForm
    success_url = reverse_lazy('login')
    template = 'blog/login.html'


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


class CommentpdateView(CreateView,LoginRequiredMixin):
    pass
class CommentCreateView(CreateView):
    pass
class CommentDeleteView(DeleteView):
    
