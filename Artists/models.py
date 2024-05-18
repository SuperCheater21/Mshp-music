from django.db import models
from Playlists.models import Playlist
from Users.models import Profile

class Artist(models.Model):
    stage_name = models.CharField(max_length=50)
    profile = models.OneToOneField(Profile)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # duration = models.CharField(max_length=20)


    def __str__(self):
        return self.title

