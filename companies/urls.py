from django.urls import path, include
from . import views
app_name = 'company'

urlpatterns = [
    path('list', views.IndexListView.as_view(), name='list'),
    path('create', views.CompanyCreateView.as_view(), name='create'),
    path('delete/<id>', views.delete, name='delete'),
]
