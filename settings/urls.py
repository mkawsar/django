from django.urls import path
from .views import *
from .views import (
    UserListView
)

urlpatterns = [
    path('', UserListView.as_view(), name='setting-index'),
    path('add/user', create, name='user-add'),
    path('delete/<user_id>/user', delete_user, name='user-delete'),
]