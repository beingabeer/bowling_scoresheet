from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game, Frame


@receiver(post_save, sender=Game)
def create_frame(sender, instance, created, *args, **kwargs):
    if created:
        frames = [
            Frame(game_id=instance, frame_no=frame_no) for frame_no in range(1, 11)
        ]
        Frame.objects.bulk_create(frames)
        f = Frame.objects.get(game_id=instance, frame_no=1)
        f.frame_is_active = True
        f.save()
