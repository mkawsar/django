from django.urls import path
from .views import *

urlpatterns = [
    path('', GroupListView.as_view(), name='group-index'),
    path('create', GroupCreateView.as_view(), name='group-create'),
    path('details/<slug>', GroupDetailsView.as_view(), name='group-details'),
    path('update/<slug>', GroupUpdateView.as_view(), name='group-update'),
    path('invite-user/<slug>', group_invite_user, name='group-user-invite'),
    path('store-invite-user', save_group_invite_user, name='store-group-user-invite'),
]
