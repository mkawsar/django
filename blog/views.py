from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
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
        context = super(PostListView, self).get_context_data(**kwargs)
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
        post_id = context['post'].pk
        context['title'] = 'Post Details'
        context['like'] = Like.objects.filter(post_id=post_id)
        context['user_like'] = Like.objects.filter(post_id=post_id).filter(user_id=self.request.user.id).first()
        context['dislike'] = Dislike.objects.filter(post_id=post_id)
        context['user_dislike'] = Dislike.objects.filter(post_id=post_id).filter(user_id=self.request.user.id).first()
        context['comments'] = Comment.objects.filter(post_id=post_id).order_by('-createdAt')
        return context


@login_required()
@csrf_exempt
def post_like(request, post_id):
    if request.is_ajax():
        user_like = Like.objects.filter(user_id=request.user.id).filter(post_id=post_id).first()
        if user_like is None:
            like = Like(like=1, post_id=post_id, user_id=request.user.id)
            like.save()
            return HttpResponse(True)
        else:
            return HttpResponse(False)


@login_required()
@csrf_exempt
def post_dislike(request, post_id):
    if request.is_ajax():
        user_dislike = Dislike.objects.filter(user_id=request.user.id).filter(post_id=post_id).first()
        if user_dislike is None:
            dislike = Dislike(dislike=1, post_id=post_id, user_id=request.user.id)
            dislike.save()
            return HttpResponse(True)
        else:
            return HttpResponse(False)


@login_required()
def comment(request):
    if request.method == 'POST':
        comment = Comment(post_id=request.POST['post_id'], comment=request.POST['comment'], user_id=request.user.id)
        comment.save()
        messages.success(request, 'Post comment added is successfully!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']
    template_name = 'blog/edit.html'
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post Update'
        context['object'] = Post.objects.filter(id=context['post'].pk).first()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post item updated successfully!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
