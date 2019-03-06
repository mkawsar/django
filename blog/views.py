from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from .models import *


# Blog post list view
class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


# Blog post create
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/create.html'
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post item created successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post Create'
        return context


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post Details'
        return context
