from django.db import models


class Song(models.Model):
    title = models.TextField()
    author = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField()
    audio_file_link = models.FileField(max_length=200, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title
