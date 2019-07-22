from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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


# Get All Users
@login_required()
def users(request):
    users = User.objects.raw("""
    SELECT auth_user.id, auth_user.first_name, auth_user.last_name, auth_user.email,
    user_profile.user_id AS user_id, user_profile.image
    FROM auth_user
    INNER JOIN user_profile
    ON auth_user.id = user_profile.user_id;
    """)
    return JsonResponse(list(users), safe=False)
