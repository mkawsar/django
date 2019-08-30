from django.urls import path, include
from .views import *

urlpatterns = [
    path('list', IndexListView.as_view(), name='company-list'),
]