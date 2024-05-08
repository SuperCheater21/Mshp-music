from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.genre_name

