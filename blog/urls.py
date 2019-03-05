from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create', PostCreateView.as_view(), name='blog-create'),
]
