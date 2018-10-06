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

    @property
    def total_points(self):
        total_points = 0

        for accomplishment in self.has_accomplished.all():
            total_points += accomplishment.points

        return total_points

    def list_accomplishments(self):
        accomplishment_list = []
        for accomplishment in self.has_accomplished.all():
            accomplishment_list.append(str(accomplishment))

        return ', '.join(accomplishment_list)


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


class Game(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_hidden = models.BooleanField(default=False)
