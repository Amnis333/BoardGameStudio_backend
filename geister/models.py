from django.db import models


class GameState(models.Model):
    table_state = models.TextField()
