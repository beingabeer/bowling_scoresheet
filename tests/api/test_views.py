import pytest

import json

from django.urls import reverse

from mixer.backend.django import mixer

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


def test_create_game(client):
    assert Game.objects.all().count() == 0

    player = mixer.blend('scoring_app.Player', player_name="Bob")

    url = reverse('api-game-create')
    data = {
        "player_id": 1
    }
    response = client.post(url, data=data, content_type="application/json")

    assert response.status_code == 201
    assert Game.objects.all().count() == 1
    assert Game.objects.first().frame_set.all().count() == 10


def test_roll_create_invalid_game_id(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)

    url = reverse('api-roll-create', kwargs={"game_id": 2})
    data = {
       'roll_one': 10,
       'roll_two': 0,
       'roll_three': 0
    }
    response = client.post(url, data=data, content_type="application/json")
    assert response.status_code == 404



def test_roll_create_400_if_game_already_over(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    mixer.blend('scoring_app.Game', player_id=player)
    game = Game.objects.all().first()
    game.in_progress = False
    game.save()
    url = reverse('api-roll-create', kwargs={"game_id": 1})
    data = {
       'roll_one': 10,
       'roll_two': 0,
       'roll_three': 0
    }
    response = client.post(url, data=data, content_type="application/json")

    assert response.status_code == 400
    assert response.data == {"detail": "This game is over"}


def test_roll_extra_frame_invalid_input(client):
    """
    For this case, roll_one and roll_two should be 0
    """
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)

    url = reverse('api-roll-create', kwargs={"game_id": 1})

    data = {
       'roll_one': 1,
       'roll_two': 5,
       'roll_three': 0
    }

    for _ in range(1, 10):
        client.post(url, data=data, content_type="application/json")

    data = {
        'roll_one': 10,
        'roll_two': 10,
        'roll_three': 0
    }

    client.post(url, data=data, content_type="application/json")

    invalid_data = {
       'roll_one': 1,
       'roll_two': 5,
       'roll_three': 0
    }
    response = client.post(url, data=invalid_data, content_type="application/json")

    assert response.status_code == 400
    assert response.data == {
                        "detail": "This is the bonus throw on frame 10, enter pins knocked value in roll_three, keeping roll_one and roll_two 0"
                    }


def test_create_roll_valid_roll(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)

    url = reverse('api-roll-create', kwargs={"game_id": 1})

    data = {
       'roll_one': 5,
       'roll_two': 5,
       'roll_three': 0
    }

    response = client.post(url, data=data, content_type="application/json")

    assert response.status_code == 201


def test_game_over_response(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)

    url = reverse('api-roll-create', kwargs={"game_id": 1})

    data = {
       'roll_one': 5,
       'roll_two': 1,
       'roll_three': 0
    }

    for _ in range(10):
        response = client.post(url, data=data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == {"detail": "Game Over!, Thanks for playing"}
