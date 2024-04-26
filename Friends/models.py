from django.db import models
from Playlists.models import Genre
from Songs.models import Song
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='media/profile_pics')

class Preference(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   favorite_genres = models.ManyToManyField(Genre)
   favorite_songs =  models.ManyToManyField(Song)

class Friend(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   friends = models.ManyToManyField(User)


