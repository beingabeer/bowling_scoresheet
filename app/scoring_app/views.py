from django.shortcuts import render, redirect
from .models import Player, Game, Frame
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
# from .forms import GameCreationForm
from django.urls import reverse_lazy


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
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PlayerCreateView(CreateView):
    model = Player
    template_name = 'scoring_app/add_player.html'
    fields = ("player_name",)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('game-list')
