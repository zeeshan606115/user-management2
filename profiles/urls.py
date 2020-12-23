from django.urls import path
from .views import my_profile_view, invites_received_view, profile_list_view, invite_profile_list_view, ProfileListView, \
    send_invitation, remove_from_friends, accept_invitation, reject_invitation, ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('', my_profile_view, name='my-profile'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('all-profiles/', ProfileListView.as_view(), name='all-profiles-view'),
    path('invite-profiles/', invite_profile_list_view, name='invite-profiles-view'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('my-invites/accept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
]