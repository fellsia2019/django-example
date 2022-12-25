# serializers.py
from rest_framework import serializers

from .models import AnimeSuperHero, MarvelSuperHero, DCSuperHero


class AnimeSuperHeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeSuperHero
        fields = ('id', 'name', 'strength', 'from_anime')


class MarvelSuperHeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarvelSuperHero
        fields = ('id', 'name', 'strength', 'from_film')


class DCSuperHeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DCSuperHero
        fields = ('id', 'name', 'strength', 'from_film')