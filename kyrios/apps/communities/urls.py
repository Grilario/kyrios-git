from django.urls import path, include

from . import views

urlpatterns = [
    path('create/', view=views.createCommunity, name="createCommunity"),
    path('enter/', view=views.enterCommunity, name="enterCommunity"),
    path('<str:communityID>/', view=views.getCommunity, name="getCommunity"),
    path('<str:communityID>/edit/', view=views.editCommunity, name="editCommunity"),
    path('<str:communityID>/delete/', view=views.deleteCommunity, name="deleteCommunity"),
    path('<str:communityID>/leave/', view=views.leave, name="leaveCommunity"),
    path('<str:communityID>/members/', view=views.listMembers, name="listCommunityMembers"),
    path('<str:communityID>/task/', include('apps.tasks.urls')),
    path('<str:communityID>/message/', include('apps.conversations.urls')),
    path('<str:communityID>/member/expulse/<str:username>', view=views.expulseMember, name="expulseMember"),
    path('<str:communityID>/member/turn-organizer/<str:username>', view=views.turnOrganizer, name="expulseMember")]
