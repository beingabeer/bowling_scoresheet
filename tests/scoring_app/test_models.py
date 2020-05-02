import pytest

from scoring_app.models import Player, Game, Frame


@pytest.mark.django_db
def test_create_player():
    player = Player(player_name='Bob')
    player.save()
    assert player.player_name == "Bob"
    assert player.player_id == 1
    assert str(player) == player.player_name



@pytest.mark.django_db
def test_create_game():
    player = Player(player_name='Bob')
    player.save()
    game = Game(player_id=player)
    game.save()

    assert game.game_id == 1
    assert game.player_id.player_id == player.player_id
    assert game.in_progress == True
    assert game.date_created
    assert game.game_score == 0
    assert str(game) == f"Game {game.game_id} - ({game.player_id})"


@pytest.mark.django_db
def test_signal_creates_ten_frames_for_each_game():
    pass


@pytest.mark.django_db
def test_first_and_last_frame_no():
    pass


@pytest.mark.django_db
def test_on_creations_first_frame_is_active():
    pass


@pytest.mark.django_db
def test_signal_creates_ten_frames_for_each_game():
    pass


@pytest.mark.django_db
def test_game_in_progress_changes_to_false_on_game_complete():
    pass


@pytest.mark.django_db
def test_cumulative_score():
    pass


@pytest.mark.django_db
def test_game_final_score():
    pass


@pytest.mark.django_db
def test_extra_frame_is_active_for_frame_10():
    pass


@pytest.mark.django_db
def test_is_strike():
    pass


@pytest.mark.django_db
def test_is_spare():
    pass


@pytest.mark.django_db
def test_max_score():
    '''
    test to check maximum score of 300 for perfect play
    '''
    pass


@pytest.mark.django_db
def test_all_spares():
    pass


@pytest.mark.django_db
def test_gutter_game():
    pass


@pytest.mark.django_db
def test_input_roles_are_valid():
    pass
