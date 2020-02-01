from django.urls import path

from .views import RatingView, RatingGetView

urlpatterns = [
    path('', RatingView.as_view(), name='list'),
    path('stars/', RatingGetView.as_view())
]
