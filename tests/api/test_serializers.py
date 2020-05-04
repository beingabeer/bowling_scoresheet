import pytest

from scoring_app.models import Player, Game, Frame

from scoring_app.api.serializers import PlayerCreateUpdateSerializer, PlayerSerializer, RollSerializer

pytestmark = pytest.mark.django_db


def test_valid_player_create_update_serializer():
    valid_serializer_data = {
        "player_name": "Bob"
    }
    serializer = PlayerCreateUpdateSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_player_create_update_serializer():
    invalid_serializer_data = {
        "player": "xyz"
    }
    serializer = PlayerCreateUpdateSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.errors == {"player_name": ["This field is required."]}


def test_valid_player_serializer():
    valid_serializer_data = {
        "player_name": "Bob"
    }
    serializer = PlayerSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_valid_roll_serializer():
    valid_serializer_data = {
        "roll_one": 5,
        "roll_two": 5,
        "roll_three": 0
    }
    serializer = RollSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}



def test_roll_serializer():
    invalid_serializer_data = {
        "roll_one": 11,
        "roll_two": 5,
        "roll_three": 0
    }
    serializer = RollSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}

