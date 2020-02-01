from rest_framework import serializers

from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializer
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ['movie', 'user', 'stars']

