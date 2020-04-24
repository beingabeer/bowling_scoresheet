from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Player, Game, Frame

admin.site.unregister(Group)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Frame)
