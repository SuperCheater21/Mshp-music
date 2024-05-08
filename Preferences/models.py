from django.db import models
from Playlists.models import Playlist

class Playlist(models.Model):
    stage_name = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    playlist = models.OneToOneField(Playlist,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

