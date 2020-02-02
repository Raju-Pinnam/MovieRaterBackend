from rest_framework import generics, mixins, status

from django.contrib.auth import get_user_model
from rest_framework.response import Response

from ratings.models import Rating
from ratings.serializers import RatingSerializer
from .models import Movie
from .serializers import MovieSerializer


class MovieListView(generics.ListAPIView):
    model = Movie
    serializer_class = MovieSerializer
    queryset = model.objects.all()


class MovieDetailView(mixins.CreateModelMixin, generics.RetrieveAPIView):
    model = Movie
    serializer_class = MovieSerializer
    queryset = model.objects.all()
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        stars = request.data.get('stars', None)
        user_slug = request.GET.get('user_slug')
        movie_slug = self.kwargs.get('slug')
        movie_obj = self.model.objects.get(slug=movie_slug)
        user_obj = get_user_model().objects.get(slug=user_slug)

        if stars is not None:
            try:
                rating_obj = Rating.objects.get(user=user_obj, movie=movie_obj)
                rating_obj.stars = stars
                rating_obj.save()
            except Rating.DoesNotExist:
                rating_obj = Rating.objects.create(user=user_obj, movie=movie_obj, stars=stars)
            serializer = RatingSerializer(rating_obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'failed'}, status=status.HTTP_400_BAD_REQUEST)

