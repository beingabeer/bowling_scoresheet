from django.urls import path

from . import views


urlpatterns = [
    path("player/create/", views.PlayerCreateAPIView.as_view(), name='api-player-create'),
    path("player-list/", views.PlayerListAPIView.as_view(), name='api-player-list'),
    path("player/<int:player_id>/", views.PlayerDetailAPIView.as_view(), name='api-player-detail'),
    path("player/<int:player_id>/delete/", views.PlayerDeleteAPIView.as_view(), name='api-player-delete'),
    path("game/create/", views.GameCreateAPIView.as_view(), name='api-game-create'),
    path("game-list/", views.GameListAPIView.as_view(), name='api-game-list'),
    # path("game/<int:game_id>/", views.GameDetailAPIView.as_view()),
    path("game/<int:game_id>/", views.GameDetail.as_view(), name='api-game-detail'),
    path("game/<int:game_id>/delete/", views.GameDeleteAPIView.as_view(), name='api-game-delete'),
    path("game/<int:game_id>/roll/", views.RollCreateAPIView.as_view(), name='api-roll-create'),
]
