from django.shortcuts import render

# views.py
from rest_framework import viewsets

from .serializers import AnimeSuperHeroSerializer, MarvelSuperHeroSerializer, DCSuperHeroSerializer
from .models import AnimeSuperHero, MarvelSuperHero, DCSuperHero


class AnimeSuperHeroViewSet(viewsets.ModelViewSet):
    queryset = AnimeSuperHero.objects.all().order_by('name')
    serializer_class = AnimeSuperHeroSerializer


class MarvelSuperHeroViewSet(viewsets.ModelViewSet):
    queryset = MarvelSuperHero.objects.all().order_by('name')
    serializer_class = MarvelSuperHeroSerializer


class DCSuperHeroViewSet(viewsets.ModelViewSet):
    queryset = DCSuperHero.objects.all().order_by('name')
    serializer_class = DCSuperHeroSerializer
