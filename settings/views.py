from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView
)


# Create your views here.
# All users list
class UserListView(ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    paginate_by = 5
