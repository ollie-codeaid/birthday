from django.conf.urls.static import static
from django.urls import path

from birthday import settings
from friends.views import (
        AccomplishmentCreate, AccomplishmentDelete,
        AccomplishmentList, AccomplishmentUpdate,
        FriendCreate, FriendDelete,
        FriendList, FriendUpdate)

urlpatterns = [
    path('', FriendList.as_view(), name='friend-list'),
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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
