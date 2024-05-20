from django.db import models
from Artists.models import Artist
from Users.utils import get_random_code
from django.template.defaultfilters import slugify
from PIL import Image
class Song(models.Model):
    song_name = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist,default=None)
    thumbnail = models.ImageField(upload_to='song_thumbnail',
                                      help_text=".jpg, .png, .jpeg, .gif, .svg supported", default='song_thumbnail/thumbnail.png')
    audio_file = models.FileField(upload_to='audio_files', help_text=".mp3 only supported")
    lyrics = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField( auto_now=True)
    #duration = models.CharField(max_length=20)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.song_name


    def save(self, *args, **kwargs):

        # creating slug
        ex = False
        if self.song_name:
            to_slug = slugify(str(self.song_name))
            if len(Song.objects.filter(slug=to_slug).all()) > 1:
                ex = True
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Song.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.song_name)
        self.slug = to_slug

        super().save(*args, **kwargs)

        # resizing images
        img = Image.open(self.thumbnail.path)

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.thumbnail.path)

        super().save(*args, **kwargs)

