from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import movie_image_path, gen_movie_slug


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=movie_image_path, null=True, blank=True)
    trailer_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'slug': self.slug})


def pre_save_funcs(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = gen_movie_slug(instance)


pre_save.connect(pre_save_funcs, sender=Movie)
