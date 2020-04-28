from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.player_name


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player_name = models.ForeignKey(Player, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    game_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Game {self.game_id} - ({self.player_name})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    @property
    def cumulative_score(self):
        frame_list = Frame.objects.filter(game_id=self)
        score = 0
        for frame in frame_list:
            score += frame.frame_score
        return score

    @property
    def final_score(self):
        if self.in_progress:
            return self.cumulative_score
        else:
            frame_list = Frame.objects.filter(game_id=self)
            score = 0
            for frame in frame_list:
                score += frame.frame_score
            self.game_score = score
            self.save()
            return score



class Frame(models.Model):
    frame_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    frame_no = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    frame_is_active = models.BooleanField(default=False)
    extra_frame_is_active = models.BooleanField(default=False)
    roll_one = models.PositiveIntegerField(default=0, choices=list(zip(range(0, 11), range(0, 11))))
    roll_two = models.IntegerField(default=0, choices=list(zip(range(0, 11), range(0, 11))))
    roll_three = models.PositiveIntegerField(default=0, choices=list(zip(range(0, 11), range(0, 11))))


    def __str__(self):
        return f"{self.game_id} Frame-{self.frame_no}"

    @property
    def input_roles_are_valid(self):
        if self.roll_one + self.roll_two > 10:
            return False
        elif self.roll_one == 10 and self.roll_two > 0:
            return False
        else:
            return True

    @property
    def is_strike(self):
        if self.roll_one == 10 and self.roll_two == 0:
            return True
        return False

    @property
    def is_spare(self):
        if not self.is_strike and self.roll_two + self.roll_one == 10:
            return True
        return False


    # recheck case logic for frame 9 and frame 10
    @property
    def frame_score(self):
        if self.roll_one + self.roll_two < 10:
            return self.roll_two + self.roll_one

        if self.is_strike and self.frame_no < 9:
            frame_one_ahead = Frame.objects.filter(game_id=self.game_id, frame_no__gt=self.frame_no).order_by('frame_no').first()
            frame_two_ahead = Frame.objects.filter(game_id=self.game_id, frame_no__gt=frame_one_ahead.frame_no).order_by('frame_no').first()

            if frame_one_ahead.is_strike:
                return 10 + 10 + frame_two_ahead.roll_one

            if not frame_one_ahead.is_strike:
                return 10 + frame_one_ahead.roll_one + frame_one_ahead.roll_two

        if self.is_spare and self.frame_no < 10:
            frame_one_ahead = Frame.objects.filter(game_id=self.game_id, frame_no__gt=self.frame_no).order_by('frame_no').first()
            return 10 + frame_one_ahead.roll_one

        # Special cases
        if self.frame_no == 9 and self.is_strike:
            frame_one_ahead = Frame.objects.filter(game_id=self.game_id, frame_no__gt=self.frame_no).order_by('frame_no').first()
            return 10 + frame_one_ahead.roll_one + frame_one_ahead.roll_two

        if self.frame_no == 10:
            if self.roll_one == 10:
                return 10 + self.roll_two + self.roll_three

            elif self.roll_one + self.roll_two == 10:
                return 10 + self.roll_three






