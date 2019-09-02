from django.urls import path, include
from .views import IndexListView, create
app_name = 'company'

urlpatterns = [
    path('list', IndexListView.as_view(), name='list'),
    path('create', create, name='create'),
]
