from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from movies.models import Movie

User = get_user_model()


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)))

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

    def __str__(self):
        return str(self.stars)

