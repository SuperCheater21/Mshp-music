from django.db import models
from Users.utils import get_random_code
from django.template.defaultfilters import slugify
from Users.models import Profile


class Artist(models.Model):
    stage_name = models.CharField(max_length=50)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    description = models.TextField(default="no description...")

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # duration = models.CharField(max_length=20)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.stage_name

    def save(self, *args, **kwargs):
        # creating slug
        ex = False
        to_slug = slugify(str(self.stage_name))
        ex = Artist.objects.filter(slug=to_slug).exists()
        while ex:
            to_slug = slugify(to_slug + " " + str(get_random_code()))
            ex = Artist.objects.filter(slug=to_slug).exists()

        self.slug = to_slug

        super().save(*args, **kwargs)
        # resizing images
