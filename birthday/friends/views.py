from django.db import transaction
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
        CreateView, DeleteView, UpdateView)
from django.views.generic.list import ListView
from friends.models import (
        Accomplishment, Friend, FriendAccomplishment)


# Create your views here.


class FriendAccomplishmentAwareMixin:
    def create_friend_accomplishments(
            self,
            form,
            field_name,
            model_name,
            model_value,
            other_model_name):

        items = form.cleaned_data[field_name]

        with transaction.atomic():
            FriendAccomplishment.objects.filter(
                    **{model_name: model_value}).delete()
            for item in items:
                friend_accomplishment = FriendAccomplishment(
                        **{
                            model_name: model_value,
                            other_model_name: item})
                friend_accomplishment.save()


class FriendCreate(FriendAccomplishmentAwareMixin, CreateView):
    model = Friend
    fields = ['name', 'mug_shot', 'has_accomplished']
    success_url = reverse_lazy('friend-list')

    def form_valid(self, form):
        friend = Friend(
                name=form.cleaned_data['name'],
                mug_shot=form.cleaned_data['mug_shot']
                )
        friend.save()

        self.create_friend_accomplishments(
                form,
                'has_accomplished',
                'friend',
                friend,
                'accomplishment')

        return HttpResponseRedirect(self.success_url)


class FriendUpdate(FriendAccomplishmentAwareMixin, UpdateView):
    model = Friend
    fields = ['name', 'mug_shot', 'has_accomplished']
    success_url = reverse_lazy('friend-list')

    def form_valid(self, form):
        friend = Friend.objects.get(pk=self.kwargs['pk'])
        friend.name = form.cleaned_data['name']
        friend.mug_shot = form.cleaned_data['mug_shot']
        friend.save()

        self.create_friend_accomplishments(
                form,
                'has_accomplished',
                'friend',
                friend,
                'accomplishment')

        return HttpResponseRedirect(self.success_url)


class FriendDelete(DeleteView):
    model = Friend
    success_url = reverse_lazy('friend-list')


class FriendList(ListView):
    model = Friend
    template_name = 'friends/friend_list.html'


class FriendLeaderboard(ListView):
    model = Friend
    template_name = 'friends/friend_leaderboard.html'


class AccomplishmentCreate(FriendAccomplishmentAwareMixin, CreateView):
    model = Accomplishment
    fields = ['description', 'points', 'accomplished_by']
    success_url = reverse_lazy('friend-list')

    def form_valid(self, form):
        accomplishment = Accomplishment(
                description=form.cleaned_data['description'],
                points=form.cleaned_data['points']
                )
        accomplishment.save()

        self.create_friend_accomplishments(
                form,
                'accomplished_by',
                'accomplishment',
                accomplishment,
                'friend')

        return HttpResponseRedirect(self.success_url)


class AccomplishmentUpdate(FriendAccomplishmentAwareMixin, UpdateView):
    model = Accomplishment
    fields = ['description', 'points', 'accomplished_by']
    success_url = reverse_lazy('friend-list')

    def form_valid(self, form):
        accomplishment = Accomplishment.objects.get(pk=self.kwargs['pk'])
        accomplishment.description = form.cleaned_data['description']
        accomplishment.points = form.cleaned_data['points']
        accomplishment.save()

        self.create_friend_accomplishments(
                form,
                'accomplished_by',
                'accomplishment',
                accomplishment,
                'friend')

        return HttpResponseRedirect(self.success_url)


class AccomplishmentDelete(DeleteView):
    model = Accomplishment
    fields = ['description', 'points', 'accomplished_by']
    success_url = reverse_lazy('friend-list')


class AccomplishmentList(ListView):
    model = Accomplishment

