from django.urls import path
from . import views

urlpatterns = [
    path('', views.bowling, name='bowling'),
    path('game/', views.game_list, name='game-list'),
    path('game/<int:pk>/', views.game_detail, name='detail'),
    path('game/new/', views.GameCreateView.as_view(), name='create-game'),
    path('player/new/', views.PlayerCreateView.as_view(), name='create-player'),
    path('game/<int:pk>/delete/', views.game_delete, name='game-delete'),
    path('bowling/', views.bowling, name='bowling')
]
