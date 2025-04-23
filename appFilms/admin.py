from django.contrib import admin
from .models import Film, Actor, ActorFilm, User, Score

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(ActorFilm)
admin.site.register(User)
admin.site.register(Score)