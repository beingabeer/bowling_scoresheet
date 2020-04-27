from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Game, Frame
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages


def bowling(request):
    return render(request, 'scoring_app/bowling.html')


def game_list(request):
    game_list = Game.objects.all()
    context = {'game_list': game_list}
    return render(request, 'scoring_app/game-list.html', context)


def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    frame_list = game.frame_set.all()
    frame_active_count = frame_list.filter(frame_is_active=True).count()
    context = {'game': game, 'frame_list': frame_list,'frame_active_count': frame_active_count}

    if request.method == "POST":
        roll_one = request.POST.get('roll_one')
        roll_two = request.POST.get('roll_two')
        current_frame = Frame.objects.get(game_id=game, frame_is_active=True)
        current_frame.roll_one = roll_one
        current_frame.roll_two = roll_two
        current_frame_num = current_frame.frame_no
        current_frame.frame_is_active = False
        current_frame.save()
        if current_frame.frame_no+1 <= 10:
            next_frame = Frame.objects.get(
                game_id=game, frame_no=current_frame_num+1)
            next_frame.frame_is_active = True
            next_frame.save()

        else:
            game.in_progress = False
            game.save()

        return render(request, 'scoring_app/detail.html', context)

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
