from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    audio_file = models.FileField(upload_to='')
    lyrics = models.TextField(blank=True, null=True)
    #duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title
