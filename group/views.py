from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import *
from django.contrib import messages


# Create your views here.
class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'group/index.html'
    context_object_name = 'groups'
    ordering = ['-createdAt']

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['title'] = 'Group'
        return context


class GroupCreateView(LoginRequiredMixin, generic.CreateView):
    model = Group
    template_name = 'group/create.html'
    fields = ['name', 'type', 'about', 'picture']
    success_url = '/group/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, 'Group item created successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Group Create'
        return context


class GroupDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Group
    template_name = 'group/details.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDetailsView, self).get_context_data(**kwargs)
        context['title'] = 'Group Details'
        return context


class GroupUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Group
    template_name = 'group/edit.html'
    fields = ['name', 'type', 'about', 'picture']
    success_url = '/group/'

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Group Update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Group item updated successfully!')
        return super().form_valid(form)


@login_required()
def group_invite_user(request, slug):
    users = User.objects.all()
    group = Group.objects.filter(slug=slug).first()
    invite_users = GroupPeople.objects.filter(group=group.id).all()
    invite_users_array = []

    for member in invite_users:
        invite_users_array.append(member.user_id)
    return render(request, 'group/invite-user.html',
                  {'users': users, 'group': group, 'invite_users': invite_users, 'user_array': invite_users_array})


@login_required()
def save_group_invite_user(request):
    try:
        if request.method == 'POST':
            users = request.POST.getlist('users[]')
            if not users:
                return JsonResponse(status=200,
                                    data={'status': False, 'message': 'Form at least one field is required'})
            for user in users:
                people = GroupPeople(group_id=request.POST['group_id'], user_id=user)
                people.save()
            return JsonResponse(status=200, data={'status': True, 'message': 'People invited successfully'})
    except:
        print(request.POST)
        return JsonResponse(status=200, data={'status': False, 'message': 'Failed to people invite!'})


@login_required()
def members(request, slug):
    group = Group.objects.filter(slug=slug).first()
    return render(request, 'group/member.html', {'group': group, 'title': 'Group Members'})


@login_required()
def delete(request, slug):
    group = Group.objects.filter(slug=slug)
    group.delete()
    messages.success(request, 'Group item deleted successfully!')
    return HttpResponseRedirect("/group/")
