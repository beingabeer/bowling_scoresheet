from django.shortcuts import render, redirect
from .models import Player, Game, Frame
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView


def bowling(request):
    return render(request, 'scoring_app/bowling.html')


def game_list(request):
    game_list = Game.objects.all()
    context = {'game_list': game_list}
    return render(request, 'scoring_app/game-list.html', context)


def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    context = {'game': game}
    return render(request, 'scoring_app/detail.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    game.delete()
    return redirect('game-list')


class GameCreateView(CreateView):
    model = Game
    template_name = "scoring_app/add_game.html"
    fields = ("player_name",)

    def form_valid(self, form):
        return super().form_valid(form)

        # return HttpResponseRedirect(self.get_success_url())


# def create_game(request):
#     if request.method == "POST":
#         player_name = request.POST.get('player_name')
#         Game.object.create(player_name=player_name)
