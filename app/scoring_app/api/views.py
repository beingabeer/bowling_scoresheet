from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from scoring_app.models import Frame, Game, Player

from .serializers import (
    GameCreateUpdateSerializer,
    GameSerializer,
    PlayerCreateUpdateSerializer,
    PlayerSerializer,
)


class PlayerCreateAPIView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateUpdateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(player_name=self.request.data['player_name'])

    def create(self, request, *args, **kwargs):
        serializer = PlayerCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailAPIView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = "player_id"


class PlayerDeleteAPIView(DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = "player_id"


class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateUpdateSerializer

    def perform_create(self, serializer):
        player_instance = get_object_or_404(
            Player, player_id=self.request.data["player_id"]
        )
        serializer.save(player_id=player_instance)


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "game_id"


class GameDeleteAPIView(DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "game_id"
