from rest_framework import serializers
from scoring_app.models import Player, Game, Frame


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'



















