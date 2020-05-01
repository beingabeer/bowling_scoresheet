from rest_framework import serializers

from scoring_app.models import Frame, Game, Player


class PlayerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("player_name",)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("player_id",)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameDetailSerializer(serializers.ModelSerializer):
    frames = serializers.SerializerMethodField()
    cumulative_score = serializers.IntegerField(read_only=True)

    def get_frames(self, game):
            return FrameSerializer(game.frame_set.all(), many=True).data

    class Meta:
        model = Game
        fields = "__all__"


class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ("frame_no", "roll_one", "roll_two", "roll_three", "frame_is_active", "extra_frame_is_active")



class RollSerializer(serializers.Serializer):
    roll_one = serializers.IntegerField(min_value=0, max_value=10)
    roll_two = serializers.IntegerField(min_value=0, max_value=10)
    roll_three = serializers.IntegerField(min_value=0, max_value=10)
