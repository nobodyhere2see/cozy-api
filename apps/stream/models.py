from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from apps.accounts.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Stream(models.Model):
    """
    This is a class for the Stream Object

    Attributes:
        channel: string that contains the source of the stream
        service: string that contains the website where the source is coming from (youtube, twitch, etc)
        live: boolean if the stream is live or not
        viewers: integer that holds the amount of current viewers
    """
    title = models.CharField(max_length = 100, default = 'New Stream')
    description = models.TextField()
    channel = models.CharField(max_length = 100, blank = True)
    service = models.CharField(max_length = 100, blank = True)
    live = models.BooleanField(default = False)
    featured = models.BooleanField(default = False)
    viewers = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

    @property
    def streamer(self):
        return self.profile

    @property
    def streamer_name(self):
        return self.profile.username