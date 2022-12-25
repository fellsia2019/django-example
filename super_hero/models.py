from django.db import models

# models.py
from django.db import models


class SuperHero(models.Model):
    name = models.CharField(max_length=60)
    strength = models.DecimalField(decimal_places=0, max_digits=100)

    def __str__(self):
        return self.name


class AnimeSuperHero(SuperHero):
    from_anime = models.CharField(max_length=255)


class MarvelSuperHero(SuperHero):
    from_film = models.CharField(max_length=255)


class DCSuperHero(MarvelSuperHero):
    pass
