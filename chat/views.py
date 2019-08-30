import os
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.contrib.auth.models import User
from django.views import generic

# Instantiate pusher
pusher = Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_APP_KEY'),
    secret=os.getenv('PUSHER_APP_SECRET'),
    cluster=os.getenv('PUSHER_APP_CLUSTER')
)


# Create your views here.
class ChatIndex(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super(ChatIndex, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'Chat'
        return context


# use the csrf_exempt decorator to exempt this function from csrf checks
@csrf_exempt
def broadcast(request):
    # collect the message from the post parameters, and save to the database
    message = Conversation(message=request.POST.get('message', ''), status='', user=request.user)
    message.save()
    # create an dictionary from the message instance so we can send only required details to pusher
    message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
    # trigger the message, channel and event to pusher
    pusher.trigger(u'a_channel', u'an_event', message)
    # return a json response of the broadcasted message
    return JsonResponse(message, safe=False)


# return all conversations in the database
def conversations(request):
    data = Conversation.objects.all()
    # loop through the data and create a new list from them. Alternatively, we can serialize the whole object and send the serialized response
    data = [{'name': person.user.username, 'status': person.status, 'message': person.message, 'id': person.id} for
            person in data]
    # return a json response of the broadcasted messgae
    return JsonResponse(data, safe=False)


# use the csrf_exempt decorator to exempt this function from csrf checks
@csrf_exempt
def delivered(request, id):
    message = Conversation.objects.get(pk=id)
    # verify it is not the same user who sent the message that wants to trigger a delivered event
    if request.user.id != message.user.id:
        socket_id = request.POST.get('socket_id', '')
        message.status = 'Delivered'
        message.save()
        message = {'name': message.user.username, 'status': message.status, 'message': message.message,
                   'id': message.id}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok')
    else:
        return HttpResponse('Awaiting Delivery')
