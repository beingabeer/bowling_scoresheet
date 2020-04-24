from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=50)


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    player_name = models.ForeignKey(Player, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=True)
    is_over = models.BooleanField(default=False)
    final_score = models.IntegerField(default=0)



class Frame(models.Model):
    frame_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    frame_no = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    roll_one = models.IntegerField()
    roll_two = models.IntegerField()
    roll_three = models.IntegerField(default=0)
    roll_four = models.IntegerField(default=0)
