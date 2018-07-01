from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from friends.models import Friend


# Create your views here.


class FriendCreate(CreateView):
    model = Friend
    fields = ['name', 'mug_shot']
    success_url = reverse_lazy('friend-list')


class FriendUpdate(UpdateView):
    model = Friend
    fields = ['name', 'mug_shot']
    success_url = reverse_lazy('friend-list')


class FriendDelete(DeleteView):
    model = Friend
    success_url = reverse_lazy('friend-list')


class FriendList(ListView):
    model = Friend
