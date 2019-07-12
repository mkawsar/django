from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.views import generic
from group.models import Group, GroupPeople


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
    p_group_count = 0
    user_count = User.objects.count()
    post_count = Post.objects.count()
    public_group = Group.objects.filter(type='public').count()
    private_group = Group.objects.filter(type='private')
    for p_group in private_group:
        p_group_count = GroupPeople.objects.filter(group_id=p_group.id).filter(user_id=request.user.id).count()
    return render(request, 'home/dashboard.html',
                  {'title': 'Home', 'user_count': user_count, 'post_count': post_count, 'public_group': public_group,
                   'p_group': p_group_count})


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


class UserDetailsView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailsView, self).get_context_data(**kwargs)
        context['title'] = 'User Page'
        user_id = context['user'].pk
        context['posts'] = Post.objects.filter(author_id=user_id).order_by('-date_posted').all()
        context['groups'] = Group.objects.filter(creator=user_id).order_by('-createdAt').all()
        return context
