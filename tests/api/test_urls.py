import pytest

from django.urls import reverse, resolve

from scoring_app.api.views import PlayerCreateAPIView, PlayerListAPIView, PlayerDetailAPIView, PlayerDeleteAPIView, GameCreateAPIView, GameListAPIView, GameDetail, GameDeleteAPIView, RollCreateAPIView

pytestmark = pytest.mark.django_db


def test_api_player_create_url_resolves():
    url = reverse('api-player-create')
    assert resolve(url).func.view_class == PlayerCreateAPIView
    assert resolve(url).route == 'api/v1/player/create/'


def test_api_player_list_url_resolves():
    url = reverse('api-player-list')
    assert resolve(url).func.view_class == PlayerListAPIView
    assert resolve(url).route == 'api/v1/player-list/'


def test_api_player_detail_url_resolves():
    url = reverse('api-player-detail', args=[1])
    assert resolve(url).func.view_class == PlayerDetailAPIView


def test_api_player_delete_url_resolves():
    url = reverse('api-player-delete', args=[1])
    assert resolve(url).func.view_class == PlayerDeleteAPIView


def test_api_game_create_url_resolves():
    url = reverse('api-game-create')
    assert resolve(url).func.view_class == GameCreateAPIView
    assert resolve(url).route == 'api/v1/game/create/'


def test_api_game_list_url_resolves():
    url = reverse('api-game-list')
    assert resolve(url).func.view_class == GameListAPIView
    assert resolve(url).route == 'api/v1/game-list/'


def test_api_game_detail_url_resolves():
    url = reverse('api-game-detail', args=[1])
    assert resolve(url).func.view_class == GameDetail


def test_api_game_detail_url_resolves():
    url = reverse('api-game-delete', args=[1])
    assert resolve(url).func.view_class == GameDeleteAPIView


def test_api_roll_create_url_resolves():
    url = reverse('api-roll-create', args=[1])
    assert resolve(url).func.view_class == RollCreateAPIView
