from django.contrib import admin

# Register your models here.
from .models import SuperHero, AnimeSuperHero, MarvelSuperHero, DCSuperHero

admin.site.register(SuperHero)
admin.site.register(AnimeSuperHero)
admin.site.register(MarvelSuperHero)
admin.site.register(DCSuperHero)
