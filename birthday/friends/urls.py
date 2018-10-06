from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from django.views.generic import TemplateView
from friends.views import (
        AccomplishmentCreate, AccomplishmentDelete,
        AccomplishmentList, AccomplishmentUpdate,
        FriendCreate, FriendDelete, FriendLeaderboard,
        FriendList, FriendUpdate, GameCreate, GameDelete,
        GameDetail, GameList, GameUpdate)

urlpatterns = [
    path('', FriendList.as_view(), name='friend-list'),
    path('leaderboard',
         FriendLeaderboard.as_view(),
         name='friend-leaderboard'),
    path('friend/add/', FriendCreate.as_view(), name='friend-add'),
    path('friend/<int:pk>/', FriendUpdate.as_view(), name='friend-update'),
    path('friend/<int:pk>/delete/',
         FriendDelete.as_view(),
         name='friend-delete'),
    path('accomplishments/',
         AccomplishmentList.as_view(),
         name='accomplishment-list'),
    path('accomplishment/add/',
         AccomplishmentCreate.as_view(),
         name='accomplishment-add'),
    path('accomplishment/<int:pk>/',
         AccomplishmentUpdate.as_view(),
         name='accomplishment-update'),
    path('accomplishment/<int:pk>/delete/',
         AccomplishmentDelete.as_view(),
         name='accomplishment-delete'),
    path('games/',
         GameList.as_view(),
         name='game-list'),
    path('game/add/',
         GameCreate.as_view(),
         name='game-add'),
    path('game/<int:pk>/',
         GameUpdate.as_view(),
         name='game-update'),
    path('game/<int:pk>/delete/',
         GameDelete.as_view(),
         name='game-delete'),
    path('game/<int:pk>/detail/',
         GameDetail.as_view(),
         name='game-detail'),
    path('map/',
         TemplateView.as_view(template_name='friends/map.html'),
         name='map'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
