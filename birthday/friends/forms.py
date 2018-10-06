from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Accomplishment, Friend, Game


class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = [
                'name',
                'mug_shot',
                'has_accomplished',
                ]
        widgets = {
                'has_accomplished': CheckboxSelectMultiple,
                }


class AccomplishmentForm(ModelForm):
    class Meta:
        model = Accomplishment
        fields = [
                'description',
                'points',
                'accomplished_by',
                ]
        widgets = {
                'accomplished_by': CheckboxSelectMultiple,
                }


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'is_hidden']
