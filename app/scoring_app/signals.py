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

        # Frame.objects.create(game_id=instance, frame_no=5)


# @receiver(post_save, sender=Game)
# def save_frame(sender, instance, *args, **kwargs):
#     instance.frame.save()
