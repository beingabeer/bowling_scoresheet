import pytest

from django.urls import reverse

from mixer.backend.django import mixer

from scoring_app.models import Player, Game, Frame

pytestmark = pytest.mark.django_db





def test_create_player():
    obj = mixer.blend('scoring_app.Player', player_name="Bob")
    assert obj.player_name == "Bob"
    assert obj.player_id == 1
    assert str(obj) == obj.player_name


def test_create_game():
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)

    assert game.game_id == 1
    assert game.player_id.player_id == player.player_id
    assert game.in_progress == True
    assert game.date_created
    assert game.game_score == 0
    assert str(game) == f"Game {game.game_id} - ({game.player_id})"



def test_automated_next_frame_is_active_after_roll(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    url = reverse("detail", kwargs={"pk": 1})
    data = {
       'roll_one': 5,
       'roll_two': 1,
       'roll_three': 0
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    frame = game.frame_set.all().filter(game_id=game).first()
    assert frame.roll_one == 5
    assert frame.roll_two == 1
    assert frame.frame_is_active == False
    next_frame = Frame.objects.filter(game_id=game, frame_no__gt=frame.frame_no).order_by("frame_no").first()
    assert next_frame.frame_is_active


def test_game_in_progress_changes_to_false_on_game_complete(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    url = reverse("detail", kwargs={"pk": 1})
    data = {
       'roll_one': 7,
       'roll_two': 2,
       'roll_three': 0
    }
    for _ in range(1, 11):
        client.post(url, data=data)

    game = Game.objects.get(player_id=player)
    assert game.in_progress == False


def test_max_score(client):
    '''
    test to check maximum score of 300 for perfect play
    '''
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    url = reverse("detail", kwargs={"pk": 1})
    data = {
       'roll_one': 10,
       'roll_two': 0,
       'roll_three': 0
    }
    for _ in range(1, 10):
        client.post(url, data=data)

    data = {
       'roll_one': 10,
       'roll_two': 10,
       'roll_three': 0
    }
    client.post(url, data=data)
    data = {
       'roll_one': 0,
       'roll_two': 0,
       'roll_three': 10
    }
    client.post(url, data=data)
    game = Game.objects.get(player_id=player)
    assert game.in_progress == False
    assert game.game_score == 300


def test_gutter_game(client):
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    url = reverse("detail", kwargs={"pk": 1})
    data = {
       'roll_one': 0,
       'roll_two': 0,
       'roll_three': 0
    }
    for _ in range(1, 11):
        client.post(url, data=data)

    game = Game.objects.get(player_id=player)
    assert game.in_progress == False
    assert game.game_score == 0


# def test_cumulative_score():
#     pass


# def test_game_final_score():
#     pass


# def test_extra_turn_in_frame_ten_on_striek_or_spare():
#     pass


# def test_is_strike():
#     pass


# def test_is_spare():
#     pass



# def test_all_spares():
#     pass




