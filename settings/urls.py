from django.urls import path
from .views import *
from .views import (
    UserListView
)

urlpatterns = [
    path('', UserListView.as_view(), name='setting-index')
]