from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='home'),
    path('settings', include('settings.urls'))
]