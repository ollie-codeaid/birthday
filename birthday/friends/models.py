from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=255)
    arrival_time = models.DateTimeField(auto_now=True)
    mug_shot = models.ImageField()
    has_accomplished = models.ManyToManyField(
            'Accomplishment',
            through='FriendAccomplishment',
            blank=True)

    def __str__(self):
        return self.name


class Accomplishment(models.Model):
    description = models.CharField(max_length=1023)
    points = models.IntegerField(default=0)
    accomplished_by = models.ManyToManyField(
            'Friend',
            through='FriendAccomplishment',
            blank=True)

    def __str__(self):
        return self.description


class FriendAccomplishment(models.Model):
    friend = models.ForeignKey(
            'Friend',
            on_delete=models.CASCADE)
    accomplishment = models.ForeignKey(
            'Accomplishment',
            on_delete=models.CASCADE)

