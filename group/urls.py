from django.urls import path
from .views import *

urlpatterns = [
    path('', GroupListView.as_view(), name='group-index'),
    path('create', GroupCreateView.as_view(), name='group-create'),
    path('details/<slug>', GroupDetailsView.as_view(), name='group-details'),
]
