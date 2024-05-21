from django.db import models
from Genres.models import Genre
from Users.models import Profile
from Artists.models import Artist
from Songs.models import Song
from PIL import Image
from Users.utils import get_random_code
from django.template.defaultfilters import slugify


# from django.core.urlresolvers import reverse

class Playlist(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, default="Anonymous", on_delete=models.CASCADE)

    # artists = models.ManyToManyField(Artist, blank=True)
    playlist_thumbnail = models.ImageField(default='playlist_pics/album.png', upload_to='playlist_pics')

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    songs = models.ManyToManyField(Song, default=None)

    is_private = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # creating slug
        ex = False

        to_slug = slugify(str(self.title))
        ex = Playlist.objects.filter(slug=to_slug).exists()
        while ex:
            to_slug = slugify(to_slug + " " + str(get_random_code()))
            ex = Playlist.objects.filter(slug=to_slug).exists()

        self.slug = to_slug

        # resizing images
        super().save(*args, **kwargs)

        # resizing images
        img = Image.open(self.playlist_thumbnail.path)

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.playlist_thumbnail.path)

        super().save(*args, **kwargs)
