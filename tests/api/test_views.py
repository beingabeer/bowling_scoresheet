import pytest

import json

from django.urls import reverse

from scoring_app.models import Player, Game, Frame

from scoring_app.api.serializers import PlayerCreateUpdateSerializer

pytestmark = pytest.mark.django_db


def test_create_player(client):
    players = Player.objects.all()
    assert players.count() == 0

    url = reverse('api-player-create')
    data = {
        "player_name": "abeer"
    }
    response = client.post(url, data=data, content_type="application/json")

    assert response.status_code == 200
    assert response.data["player_name"] == "abeer"

    players = Player.objects.all()
    assert players.count() == 1
