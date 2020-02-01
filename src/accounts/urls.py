from django.urls import path

from .views import UserView, UserDetailView

urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('<slug:slug>/', UserDetailView.as_view(), name="details")
]
