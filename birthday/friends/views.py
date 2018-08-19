from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import (
        CreateView, DeleteView, UpdateView)
from django.views.generic.list import ListView
from friends.forms import AccomplishmentForm, FriendForm, GameForm
from friends.models import (
        Accomplishment, Friend, FriendAccomplishment, Game)


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


class FriendCreate(
        LoginRequiredMixin,
        FriendAccomplishmentAwareMixin,
        CreateView):
    model = Friend
    form_class = FriendForm
    login_url = '/admin/login'
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


class FriendUpdate(
        LoginRequiredMixin,
        FriendAccomplishmentAwareMixin,
        UpdateView):
    model = Friend
    form_class = FriendForm
    login_url = '/admin/login'
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


class FriendDelete(LoginRequiredMixin, DeleteView):
    model = Friend
    login_url = '/admin/login'
    success_url = reverse_lazy('friend-list')


class FriendList(ListView):
    model = Friend
    template_name = 'friends/friend_list.html'


class FriendLeaderboard(ListView):
    model = Friend
    template_name = 'friends/friend_leaderboard.html'


class AccomplishmentCreate(
        LoginRequiredMixin,
        FriendAccomplishmentAwareMixin,
        CreateView):
    model = Accomplishment
    form_class = AccomplishmentForm
    login_url = '/admin/login'
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


class AccomplishmentUpdate(
        LoginRequiredMixin,
        FriendAccomplishmentAwareMixin,
        UpdateView):
    model = Accomplishment
    form_class = AccomplishmentForm
    login_url = '/admin/login'
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


class AccomplishmentDelete(LoginRequiredMixin, DeleteView):
    model = Accomplishment
    login_url = '/admin/login'
    success_url = reverse_lazy('friend-list')


class AccomplishmentList(ListView):
    model = Accomplishment


class GameCreate(
        LoginRequiredMixin,
        CreateView):
    model = Game
    form_class = GameForm
    login_url = '/admin/login'
    success_url = reverse_lazy('game-list')


class GameUpdate(
        LoginRequiredMixin,
        UpdateView):
    model = Game
    form_class = GameForm
    login_url = '/admin/login'
    success_url = reverse_lazy('game-list')


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    login_url = '/admin/login'
    success_url = reverse_lazy('game-list')


class GameList(ListView):
    model = Game


class GameDetail(DetailView):
    model = Game
