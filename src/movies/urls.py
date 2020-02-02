from django.urls import path

from .views import MovieDetailView, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='detail')
]
