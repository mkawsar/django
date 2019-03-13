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
