from . import views
from django.urls import path
app_name = 'company'

urlpatterns = [
    path('list', views.IndexListView.as_view(), name='list'),
    path('create', views.CompanyCreateView.as_view(), name='create'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<slug>', views.CompanyUpdateView.as_view(), name='update'),
    path('details/<slug>', views.CompanyDetailsView.as_view(), name='details'),
]
