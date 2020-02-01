from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from movies.models import Movie
from .models import Rating
from .serializers import RatingSerializer

User = get_user_model()


class RatingView(generics.ListAPIView):
    model = Rating
    queryset = model.objects.all()
    serializer_class = RatingSerializer


class RatingGetView(generics.RetrieveAPIView):
    model = Rating
    queryset = model.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        user_slug = request.GET.get('user_slug')
        movie_slug = request.GET.get('movie_slug')
        movie_obj = None
        user_obj = None
        if movie_slug:
            movie_obj = Movie.objects.get(slug=movie_slug)
        if user_slug:
            user_obj = User.objects.get(slug=user_slug)
        rating_obj = None
        if movie_obj and user_obj:
            try:
                rating_obj = Rating.objects.get(movie=movie_obj, user=user_obj)
            except Rating.DoesNotExist:
                pass
        return Response(self.serializer_class(rating_obj, many=False).data, status=status.HTTP_200_OK)
