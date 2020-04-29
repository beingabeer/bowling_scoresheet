from django.urls import path
from . import views

urlpatterns = [
        path("player-list", views.PlayerListAPIView.as_view()),
        path("player/<int:player_id>", views.PlayerDetailAPIView.as_view()),
        path("game-list", views.GameListAPIView.as_view()),
        path("game/<int:game_id>", views.GameDetailAPIView.as_view()),
]
