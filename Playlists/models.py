from django.db import models
from Songs.models import Song
from Genres.models import Genre
from Users.models import Profile
#from django.core.urlresolvers import reverse

class Playlist(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='playlist_pics')
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.title