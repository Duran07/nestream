from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=150)
    workers_count = models.PositiveIntegerField()
    games_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name

