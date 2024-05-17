from django.db import models
from Playlists.models import Playlist
from Users.models import Profile

class Song(models.Model):
    song_name = models.CharField(max_length=50)
    album = models.ForeignKey(Playlist, on_delete=models.CASCADE,default=None)
    artists = models.ManyToManyField(Profile,default=None ,blank=True)
    thumbnail = models.ImageField(upload_to='audio_files/images',
                                      help_text=".jpg, .png, .jpeg, .gif, .svg supported", blank=True)
    audio_file = models.FileField(upload_to='audio_files', help_text=".mp3 only supported")
    lyrics = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField( auto_now=True)
    #duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title