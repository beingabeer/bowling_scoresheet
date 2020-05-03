import pytest

from mixer.backend.django import mixer

from scoring_app.models import Player, Game, Frame

pytestmark = pytest.mark.django_db

def test_signal_creates_ten_frames_for_each_game():
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    assert game.frame_set.all().count() == 10, 'signal should create 10 frames for each game'


def test_first_and_last_frame_no():
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    assert game.frame_set.first().frame_no == 1 , 'frame no should be 1'
    assert game.frame_set.last().frame_no == 10, 'frame no should be 10'


def test_on_creation_only_first_frame_is_active():
    player = mixer.blend('scoring_app.Player', player_name="Bob")
    game = mixer.blend('scoring_app.Game', player_id=player)
    frame_list = game.frame_set.all().filter(game_id=game, frame_is_active=True)
    assert frame_list.count() == 1, 'only one frame should be active at a time'
    assert frame_list.first().frame_no == 1, 'first frame should be active'

    for frame in frame_list[1:]:
        assert frame.frame_is_active == False, 'Only first frame should be active'
