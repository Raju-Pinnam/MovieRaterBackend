from django.contrib.auth import get_user_model
from rest_framework import generics, mixins

from .serializers import UserSerializer

User = get_user_model()


class UserView(mixins.CreateModelMixin, generics.ListAPIView):
    """Used for getting List of users may used for search. Iam not implementing it."""
    model = User
    queryset = model.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    model = User
    queryset = model.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
