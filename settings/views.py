from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView
)


# All users list
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    ordering = ['-date_joined']
    paginate_by = 5
