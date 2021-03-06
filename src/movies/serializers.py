from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'slug', 'image', 'trailer_url', 'get_absolute_url', 'get_num_of_ratings',
                  'get_avg_rating']
        read_only_fields = ['id', 'get_absolute_url']
