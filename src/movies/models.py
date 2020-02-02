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

    def get_num_of_ratings(self):
        return self.rating_set.all().count()

    def get_avg_rating(self):
        avg = 0
        if self.get_num_of_ratings() > 0:
            total_ratings = 0
            for rate_obj in self.rating_set.all():
                total_ratings += rate_obj.stars
            avg = total_ratings / self.get_num_of_ratings()
        return avg


def pre_save_funcs(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = gen_movie_slug(instance)


pre_save.connect(pre_save_funcs, sender=Movie)
