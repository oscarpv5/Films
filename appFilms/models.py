from django.db import models
from django.db.models import SET_NULL

class Film(models.Model):
    title = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Actor(models.Model):
    actorName = models.CharField(max_length=50)
    actorLastName = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.actorName

class ActorFilm(models.Model):
    title = models.ForeignKey("Film", on_delete=SET_NULL, null=True)
    actorName = models.ForeignKey("Actor", on_delete=SET_NULL, null=True)

    def __str__(self):
        return "Title: " + str(self.title) + ", Actor: " + str(self.actorName)

class User(models.Model):
    userId = models.CharField(primary_key=True, max_length=50)
    userName = models.CharField(max_length=50, null=True)
    userLastName = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.userName

class Score(models.Model):
    filmScore = models.IntegerField()
    film = models.ForeignKey("Film", on_delete=SET_NULL, null=True)
    userName = models.ForeignKey("User", on_delete=SET_NULL, null=True)

    def __str__(self):
        return "Score: " + str(self.filmScore) + ", Film: " + str(self.film) + ", User: " + str(self.userName)

'''
class Seleccion(models.Model):
    nombre = models.CharField(max_lenght=50)

class Equipo(models.Model):
    nombre = models.CharField(max_lenght=50)

class Jugador(models.Model):
    nombre = models.CharField(max_lenght=50)
    posicion = models.CharField(max_lenght=50)
    equipo = models.ForeignKey("Equipo", on_delete=SET_NULL, null=True)
    seleccion = models.ForeignKey("Seleccion", on_delete=SET_NULL, null=True)

class Competicion(models.Model):
    categoria = models.CharField(max_lenght=50)
    type = models.CharField(max_length=2, choices=[
        ('EQ', 'Equipo'),
        ('SE', 'Seleccion'),
    ])

class EquipoCompeticion(models.Model):
    equipo = models.ForeignKey("Equipo", on_delete=SET_NULL, null=True)
    competicion = models.ForeignKey("Competicion", on_delete=SET_NULL, null=True)

class SeleccionCompeticion(models.Model):
    seleccion = models.ForeignKey("Seleccion", on_delete=SET_NULL, null=True)
    competicion = models.ForeignKey("Competicion", on_delete=SET_NULL, null=True)

class EquipoPartido(models.Model):
    equipo1 = models.ForeignKey("Equipo", on_delete=SET_NULL, null=True)
    equipo2 = models.ForeignKey("Equipo", on_delete=SET_NULL, null=True)
    competicion = models.ForeignKey("Competicion", on_delete=SET_NULL, null=True)

class SeleccionPartido(models.Model):
    seleccion1 = models.ForeignKey("Seleccion", on_delete=SET_NULL, null=True)
    seleccion2 = models.ForeignKey("Seleccion", on_delete=SET_NULL, null=True)
    competicion = models.ForeignKey("Competicion", on_delete=SET_NULL, null=True)
'''