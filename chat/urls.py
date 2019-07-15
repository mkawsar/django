from django.urls import path
from .views import *

urlpatterns = [
    path('', ChatIndex.as_view(), name='chat-index')
]