from rest_framework import serializers
from scoring_app.models import Player, Game, Frame


class PlayerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_name',)


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        


class GameCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('player_id',)


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'




