from django.urls import path, include
from .views import IndexListView, CompanyCreateView
app_name = 'company'

urlpatterns = [
    path('list', IndexListView.as_view(), name='list'),
    path('create', CompanyCreateView.as_view(), name='create'),
]
