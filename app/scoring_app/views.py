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
        current_frame = Frame.objects.get(game_id=game, frame_is_active=True)
        if current_frame.extra_frame_is_active:
            roll_three = int(request.POST.get('roll_three'))
            current_frame.roll_three = roll_three
            current_frame.frame_is_active = False
            current_frame.extra_frame_is_active = False
            current_frame.save()
            game.in_progress = False
            game.save()
            messages.success(request, f"Game Over! Thanks for playing!")

        else:
            roll_one = int(request.POST.get('roll_one'))
            roll_two = int(request.POST.get('roll_two'))
            current_frame = Frame.objects.get(game_id=game, frame_is_active=True)

            if current_frame.frame_no == 10:
                if (roll_one == 10) or (roll_one + roll_two) >= 10:
                    current_frame.roll_one = roll_one
                    current_frame.roll_two = roll_two
                    current_frame.extra_frame_is_active = True
                    current_frame.save()
                    return render(request, 'scoring_app/detail.html', context)
                else:
                    current_frame.roll_one = roll_one
                    current_frame.roll_two = roll_two
                    current_frame.frame_is_active = False
                    current_frame.extra_frame_is_active = False
                    current_frame.save()
                    game.in_progress = False
                    game.save()
                    messages.success(request, f"Game Over! Thanks for playing!")
                    return render(request, 'scoring_app/detail.html', context)

            elif roll_one == 10 and roll_two > 0:
                messages.warning(request, f"Roll one is a strike! Roll 2 should be zero")
                return render(request, 'scoring_app/detail.html', context)

            elif roll_one + roll_two > 10:
                messages.warning(request, f"Cannot knock more than 10 pins in one frame!")
                return render(request, 'scoring_app/detail.html', context)

            else:
                current_frame.roll_one = roll_one
                current_frame.roll_two = roll_two
                current_frame.frame_is_active = False
                current_frame.save()
                if current_frame.frame_no+1 <= 10:
                    next_frame = Frame.objects.filter(game_id=game, frame_no__gt=current_frame.frame_no).order_by('frame_no').first()
                    next_frame.frame_is_active = True
                    next_frame.save()

                else:
                    game.in_progress = False
                    game.save()
                    messages.success(request, f"Game Over! Thanks for playing!")

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
