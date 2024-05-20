from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50,blank=True, unique=True)

    def __str__(self):
        return self.name

