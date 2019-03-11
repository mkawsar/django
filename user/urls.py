from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='home'),
    path('profile', profile, name='profile'),
    path('user/<int:pk>/details', UserDetailsView.as_view(), name='user-details'),
    path('settings/', include('settings.urls')),
    path('blog/', include('blog.urls'))
]
