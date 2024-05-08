from django.db import models
from Songs.models import Song
from Genres.models import Genre


class Playlist(models.Model):
    title = models.TextField()
    author = models.TextField()
    image = models.ImageField()
    songs = models.ManyToManyField(Song)
    genre = models.OneToOneField(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.title