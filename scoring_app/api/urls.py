from django.urls import path

from . import views


urlpatterns = [
    path("player/create/", views.PlayerCreateAPIView.as_view()),
    path("player-list/", views.PlayerListAPIView.as_view()),
    path("player/<int:player_id>/", views.PlayerDetailAPIView.as_view()),
    path("player/<int:player_id>/delete/", views.PlayerDeleteAPIView.as_view()),
    path("game/create/", views.GameCreateAPIView.as_view()),
    path("game-list/", views.GameListAPIView.as_view()),
    # path("game/<int:game_id>/", views.GameDetailAPIView.as_view()),
    path("game/<int:game_id>/", views.GameDetail.as_view()),
    path("game/<int:game_id>/delete/", views.GameDeleteAPIView.as_view()),
    path("game/<int:game_id>/roll/", views.RollCreateAPIView.as_view()),
]
