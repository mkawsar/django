from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create', PostCreateView.as_view(), name='blog-create'),
    path('details/<slug>', PostDetailView.as_view(), name='blog-detail'),
    path('post/like/<post_id>', post_like, name='post-like'),
    path('post/dislike/<post_id>', post_dislike, name='post-dislike'),
    path('post/comment', comment, name='post-comment'),
]
