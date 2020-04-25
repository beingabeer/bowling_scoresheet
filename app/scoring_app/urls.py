from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:pk>/', views.game_detail, name='detail'),
    path('game/new/', views.GameCreateView.as_view(), name='create'),
    path('game/<int:pk>/delete/', views.game_delete, name='game-delete'),
]
