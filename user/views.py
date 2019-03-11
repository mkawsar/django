from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required


# Registration page and store
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created. You are now enable to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


# Design of home page
@login_required()
def dashboard(request):
    user_count = User.objects.count()
    post_count = Post.objects.count()
    return render(request, 'home/dashboard.html', {'title': 'Home', 'user_count': user_count, 'post_count': post_count})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
    return render(request, 'profile/index.html', {'title': 'Profile Edit'})
