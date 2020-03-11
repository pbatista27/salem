from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#models
from .models import Post
# Create your views here.
class Posts(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    queryset = Post.objects.filter(estado='publicado')

class PostsDetalle(DetailView):
    queryset = Post.objects.filter(estado='publicado')
    template_name = 'blog/post_detail.html'