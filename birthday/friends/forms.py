from django.forms import ModelForm

from .models import Accomplishment, Friend


class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = [
                'name',
                'mug_shot',
                'has_accomplished',
                ]


class AccompishmentForm(ModelForm):
    class Meta:
        model = Accomplishment
        fields = [
                'description',
                'points',
                'accomplished_by',
                ]
