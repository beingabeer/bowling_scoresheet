import pytest

from pytest_django.asserts import assertTemplateUsed

from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_bowling_view(client):
   url = reverse('bowling')
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed  == 'bowling.html'


def test_game_list_view(client):
   url = reverse('game-list')
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed  == 'game-list.html'


def test_player_create_view(client):
   url = reverse('create-player')
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed == "add_player.html"




def test_game_create_view(client):
   url = reverse('create-game')
   response = client.get(url)
   assert response.status_code == 200
   assertTemplateUsed == "add_game.html"



