import pytest

from scoring_app.api.serializers import PlayerCreateUpdateSerializer

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
