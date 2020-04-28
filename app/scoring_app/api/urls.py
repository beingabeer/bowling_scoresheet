from django.urls import path
from . import views

urlpatterns = [
        path("", views.PlayerListAPIView.as_view()),
]

