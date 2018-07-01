from django.conf.urls.static import static
from django.urls import path

from birthday import settings
from friends.views import (FriendCreate, FriendDelete,
                           FriendList, FriendUpdate)

urlpatterns = [
    path('', FriendList.as_view(), name='friend-list'),
    path('friend/add/', FriendCreate.as_view(), name='friend-add'),
    path('friend/<int:pk>/', FriendUpdate.as_view(), name='friend-update'),
    path(
        'friend/<int:pk>/delete/',
        FriendDelete.as_view(),
        name='friend-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
