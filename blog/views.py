from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import *
from django.views.decorators.csrf import csrf_exempt


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


@login_required()
@csrf_exempt
def post_like(request, post_id):
    if request.is_ajax():
        data = request.POST
        post_like = PostLike.objects.filter(post_id=post_id).first()
        if post_like is None:
            like = PostLike(like=data['likeCount'], post_id=post_id)
            like.save()
            Post.objects.filter(id=data['postID']).update(like=like.id)
        else:
            PostLike.objects.filter(post_id=post_id).update(like=data['likeCount'])

        return HttpResponse(data)
