from django.db import models
from django.utils.text import slugify
# Create your models here.

# save a shortened link

# * name
# * url
# * slug
# * no. of clicks


class Link(models.Model):
    name = models.CharField(unique = True, max_length=50)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} | {}".format(self.name, self.clicks)

    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)