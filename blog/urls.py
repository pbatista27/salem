from django.urls import path
from .views import Posts, PostsDetalle
from .models import Post
urlpatterns = [
    path('', Posts.as_view(), name='posts_list'),
    path('<slug:slug>', PostsDetalle.as_view(model=Post), name='post_detail')
]