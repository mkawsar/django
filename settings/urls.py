from django.urls import path
from .views import *

urlpatterns = [
    path('', setting_index, name='setting-index')
]