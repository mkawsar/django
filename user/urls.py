from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='home'),
    path('profile', profile, name='profile'),
    path('settings/', include('settings.urls'))
]