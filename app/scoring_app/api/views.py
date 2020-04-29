from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from scoring_app.models import Player, Game, Frame
from .serializers import PlayerListSerializer, PlayerDetailSerializer, GameListSerializer, GameDetailSerializer


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerListSerializer

class PlayerDetailAPIView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer
    lookup_field = 'player_id'


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer
    lookup_field = 'game_id'