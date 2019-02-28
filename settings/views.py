from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView
)
from user.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# All users list
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    ordering = ['first_name']
    paginate_by = 5


# Add new user
@login_required()
def create(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registration by admin is successfully!')
            return redirect('setting-index')
    return render(request, 'user/add.html', {'title': 'New User'})


# Delete user
@login_required()
def delete_user(request, user_id):
    try:
        u = User.objects.get(id=user_id)
        u.delete()
        messages.success(request, 'User delete successfully!')
        return redirect('setting-index')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist!')
        return redirect('setting-index')
    except Exception as e:
        messages.error(request, 'Failed to user delete!')
        return redirect('setting-index')
