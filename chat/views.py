from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic


# Create your views here.
class ChatIndex(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super(ChatIndex, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'Chat'
        return context
