from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    GameDetailSerializer,
    RollSerializer,
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


# class GameDetailAPIView(RetrieveAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameDetailSerializer
#     lookup_field = "game_id"


class GameDetail(APIView):
    def get_object(self, game_id):
        try:
            return Game.objects.get(game_id=game_id)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, game_id, format=None):
        game = self.get_object(game_id)
        serializer = GameDetailSerializer(game)
        return Response(serializer.data)


class RollCreateAPIView(CreateAPIView):
    serializer_class = RollSerializer

    def post(self, request, game_id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        try:
            game = Game.objects.get(game_id=game_id)
        except Game.DoesNotExist:
            raise Http404

        if not game.in_progress:
            return Response(
                {"detail": "This game is over"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            current_frame = Frame.objects.get(game_id=game, frame_is_active=True)
        except Frame.DoesNotExist:
            raise Http404

        if current_frame.extra_frame_is_active:
            roll_three = validated_data["roll_three"]
            current_frame.roll_three = roll_three
            current_frame.frame_is_active = False
            current_frame.extra_frame_is_active = False
            current_frame.save()
            game.in_progress = False
            game.final_score
            game.save()
            return Response(
                {"detail": "Game Over!, Thanks for playing"},
                status=status.HTTP_201_CREATED,
            )

        else:
            roll_one = validated_data["roll_one"]
            roll_two = validated_data["roll_two"]
            current_frame = Frame.objects.get(game_id=game, frame_is_active=True)

            if current_frame.frame_no == 10:
                if (roll_one == 10) or (roll_one + roll_two) >= 10:
                    current_frame.roll_one = roll_one
                    current_frame.roll_two = roll_two
                    current_frame.extra_frame_is_active = True
                    current_frame.save()
                    return Response(status=status.HTTP_201_CREATED)

                else:
                    current_frame.roll_one = roll_one
                    current_frame.roll_two = roll_two
                    current_frame.frame_is_active = False
                    current_frame.extra_frame_is_active = False
                    current_frame.save()
                    game.in_progress = False
                    game.final_score
                    game.save()
                    return Response(
                        {"detail": "Game Over!, Thanks for playing"},
                        status=status.HTTP_201_CREATED,
                    )

            elif roll_one == 10 and roll_two > 0:
                return Response(
                    {
                        "detail": "Roll one is a strike! Roll 2 cannot be greater than zero"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            elif roll_one + roll_two > 10:
                return Response(
                    {"detail": "Cannot knock more than 10 pins in one frame!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            else:
                current_frame.roll_one = roll_one
                current_frame.roll_two = roll_two
                current_frame.frame_is_active = False
                current_frame.save()
                if current_frame.frame_no + 1 <= 10:
                    next_frame = (
                        Frame.objects.filter(
                            game_id=game, frame_no__gt=current_frame.frame_no
                        )
                        .order_by("frame_no")
                        .first()
                    )
                    next_frame.frame_is_active = True
                    next_frame.save()

                else:
                    game.in_progress = False
                    game.final_score
                    game.save()
                    return Response(
                        {"detail": "Game Over!, Thanks for playing"},
                        status=status.HTTP_201_CREATED,
                    )

        return Response(status=status.HTTP_201_CREATED)


class GameDeleteAPIView(DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "game_id"
