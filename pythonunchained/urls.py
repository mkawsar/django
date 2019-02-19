from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include('user.urls'))
]
