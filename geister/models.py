from django.db import models


class GameState(models.Model):
    players = models.JSONField(default=list)
    table = models.JSONField(default=list)
    winner = models.CharField(max_length=255, default="")
    turn = models.IntegerField(default=0)