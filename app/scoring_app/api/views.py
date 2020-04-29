from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from scoring_app.models import Player, Game, Frame
from .serializers import PlayerCreateUpdateSerializer ,PlayerListSerializer, PlayerDetailSerializer, GameCreateUpdateSerializer, GameListSerializer, GameDetailSerializer
from django.shortcuts import get_object_or_404


class PlayerCreateAPIView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(player_name=self.request.data['player_name'])


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerListSerializer

class PlayerDetailAPIView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer
    lookup_field = 'player_id'

class PlayerDeleteAPIView(DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer
    lookup_field = 'player_id'


class GameCreateAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateUpdateSerializer

    def perform_create(self, serializer):
        player_instance = get_object_or_404(Player, player_id=self.request.data['player_id'])
        serializer.save(player_id=player_instance)


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer


class GameDetailAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer
    lookup_field = 'game_id'
