from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=50)

    def __str__(self):
        return self.player_name


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player_name = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player')
    in_progress = models.BooleanField(default=True)
    final_score = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Game {self.game_id} - ({self.player_name})"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


class Frame(models.Model):
    frame_id = models.AutoField(primary_key=True)
    # frame_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    game_id = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game')
    # frame_no = models.IntegerField(choices=list(
    #     zip(range(1, 11), range(1, 11))))
    frame_no = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    roll_one = models.IntegerField(default=0)
    roll_two = models.IntegerField(default=0)
    roll_three = models.IntegerField(default=0)
    roll_four = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.game_id} Frame-{self.frame_no}"
