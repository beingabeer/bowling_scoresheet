from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Frame, Game, Player


admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Frame)
