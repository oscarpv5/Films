from django.db import models
from django.db.models import SET_NULL

class Film(models.Model):
    title = models.CharField(primary_key=True, max_length=50)

class Actor(models.Model):
    actorName = models.CharField(max_lenght=50)

class ActorFilm(models.Model):
    title = models.ForeignKey("Film", on_delete=SET_NULL, null=True)
    actorName = models.ForeignKey("Actor", on_delete=SET_NULL, null=True)

class User(models.Model):
    userName = models.CharField(primary_key=True, max_lenght=50)

class Score(models.Model):
    filmScore = models.IntegerField()
    film = models.ForeignKey("Film", on_delete=SET_NULL, null=True)
    userName = models.ForeignKey("User", on_delete=SET_NULL, null=True)