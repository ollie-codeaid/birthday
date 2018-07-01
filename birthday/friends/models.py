from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=255)
    arrival_time = models.DateTimeField(auto_now=True)
    mug_shot = models.ImageField()
