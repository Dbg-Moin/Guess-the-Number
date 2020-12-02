from django.urls import path

from guess_game.views import guess_game

urlpatterns = [
    path('', guess_game)
]
