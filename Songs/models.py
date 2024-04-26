from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    #image = models.ImageField()
    audio_file = models.FileField(upload_to='')
    #audio_file_link = models.FileField(max_length=200, blank=True, null=True, upload_to='media/')
    #lyrics = models.TextField(blank=True, null=True)
    #duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title
