from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .utils import get_random_code
from django.template.defaultfilters import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    updated = models.DateTimeField(auto_now=True)
    bio = models.TextField(default='no bio...', max_length=300)
    slug = models.SlugField( unique=True,blank=True)

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):

        # creating slug
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug

        # resizing images
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)

        super().save(*args, **kwargs)
