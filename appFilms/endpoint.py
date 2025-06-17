import json
from datetime import datetime
import secrets

from django.http import JsonResponse
from appFilms.models import Film, Actor, User, ActorFilm, Score
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db import IntegrityError


def prueba1(request):
    return JsonResponse({})
# print/JSON1
# devuelve un json vacio

def prueba2(request, valor1, valor2):
    return JsonResponse(
        {
            "Estado": valor1,
            "Nuevo estado": valor2
        })
# print/<valor1>/JSON2/<valor2>
# devuelve un json con valores que se le asignan en la ruta (numericos y string)

def prueba3(request, valor):
    return JsonResponse({"Estado": valor})
# print/JSON3/<valor>
# devuelve un json con el valor que se le asigna en la ruta (numerico o string)

def prueba4(request, valor):
    return JsonResponse({"Estado": valor})
# print/JSON4/<int:valor>
# devuelve un json con el valor que se le asigna en la ruta (solo numerico)

def prueba5(request):
    if request.method == "GET":
        q = request.GET.get('q')
        print(f"Query param q: {q}")
        return JsonResponse({'query': q})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# print/JSON5?q=...
# query param que devuelve un json con el valor que se le asigna en la ruta (numerico o string)

def prueba6(request, valor):
    if request.method == "GET":
        q = request.GET.get('q')
        print(f"Query param q: {q}")
        return JsonResponse({'valor': valor, 'query': q})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# print/JSON6/<int:valor> (2?q=...)
# devuelve un json con los valores que se le asignan en la ruta (path param numerico el 1º, query param numerico o string el 2º)

def prueba7(request):
    if request.method == "GET":
        q = request.GET.get('q')
        p = request.GET.get('p')
        print(f"q = {q}, p = {p}")
        return JsonResponse({'q': q, 'p': p})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# print/JSON7?q=...&p=...
# query param que devuelve un json con los valores que se le asignan en la ruta (numericos o string)

def titulo(request, title):
    if request.method == "GET":
        try:
            x = Film.objects.get(title=title) # compara el titulo recibido con la base de datos
            return JsonResponse({
                "title": x.title
            })
        except Film.DoesNotExist:
            return JsonResponse({"error": "The movie with that title has not been found"}, status=404)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# films/<title>
# devuelve un json con el nombre del titulo que previamente verifica si esta en la base de datos

def peliculas(request):
    if request.method == "GET":

        s = request.GET.get("search")

        if s is None:
            peliculas = Film.objects.all()
        else:
            peliculas = Film.objects.filter(Q(title__icontains=s) | Q(synopsis__icontains=s)) #sensibilidad entre mayusculas y minusculas

        data = []
        for pelicula in peliculas:
            data.append({ # el append agrega un diccionario a data que es un array
                "Id": pelicula.id,
                "Title": pelicula.title,
                "Synopsis": pelicula.synopsis,
                "Year": pelicula.year
            })
        return JsonResponse(data, safe=False, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# films/
# devuelve un json con los campos de id, title, synopsis y year de todas las peliculas

# films/?search=...
# devuelve un json con los campos de id, title, synopsis y year en las que aparezca lo que se busca en la ruta

def actores(request):
    if request.method == "GET":
        actores = Actor.objects.all()

        data = [{ # se agrega un diccionario a data que es un array
            "Id": actor.id,
            "Name": actor.actorName,
            "Last name": actor.actorLastName,
            "Gender": actor.gender
        } for actor in actores]

        return JsonResponse(data, safe=False, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)
# actors/
# devuelve un json con los campos de id, name, last name y gender de todos los actores

@csrf_exempt
def usuarios(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)

        try:
            userId = json_data['userId']
            userName = json_data['userName']
            userLastName = json_data['userLastName']
            password = json_data['password']

            newUser = User.objects.create(userId = userId, userName = userName, userLastName = userLastName, password = password)

            idUsuario = newUser.userId
            nameUsuario = newUser.userName
            lastNameUsuario = newUser.userLastName
            contrasena = newUser.password

        except IntegrityError:
            return JsonResponse({"error": "userId already exists in DB"}, status=409)
        except KeyError:
            return JsonResponse({"error": "Missing field"}, status=400)

        return JsonResponse({"userId": idUsuario, "userName": nameUsuario, "userLastName": lastNameUsuario, "password": contrasena}, status=201)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

@csrf_exempt
def personas(request):
    if request.method == "POST":

        json_data = json.loads(request.body)

        nombre = json_data['nombre']
        fecha = json_data['fecha_nacimiento']
        feliz = json_data['es_feliz']
        clave = json_data['clave_felicidad'].lower()

        formato = "%d/%m/%Y"
        fecha_nacimiento = datetime.strptime(fecha, formato)

        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year

        print(f"La persona se llama {nombre}, tiene {edad} años, {'es' if feliz else 'no es'} feliz. Su clave para la felicidad es {clave}")

        return JsonResponse({}, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

@csrf_exempt
def digimons(request):
    if request.method == "POST":

        json_data = json.loads(request.body)

        print("La lista de digimons es:")

        for digimon in json_data['digimons']:
            nombre = digimon['nombre']
            mensaje = f"El nombre es {nombre}."

            if 'evoluciones' in digimon:
                mensaje = mensaje + f" Sus evoluciones son "
                for evolucion in digimon['evoluciones']:
                    mensaje = mensaje + evolucion + " "

            if 'evoluciones_oscuras' in digimon and digimon["evoluciones_oscuras"] != []:
                mensaje = mensaje + f". Sus evoluciones oscuras son "
                for evolucion_oscuras in digimon['evoluciones_oscuras']:
                    mensaje = mensaje + evolucion_oscuras + " "

            print(mensaje)

        return JsonResponse({}, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body)

            try:
                usuario = json_data["username"]
                user = User.objects.get(userId = usuario)
                contrasena = json_data["password"]

                if user.password == contrasena:
                    token = secrets.token_hex(32)
                    user.tokenSesion = token
                    user.save()

                    print("Contraseña correcta")
                else:
                    print("Contraseña incorrecta")

            except User.DoesNotExist:
                return JsonResponse({"error": "Not that User in database"}, status=400)

            print("Usuario: " + usuario)
            print("Contraseña: " + contrasena)

        except KeyError:
            return JsonResponse({"error": "Missing user and/or password"}, status=400)

        return JsonResponse({"token": token}, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def peliculaId(request, id):
    if request.method == "GET":
        try:
            x = Film.objects.get(id = id) # busca en base de datos de Film el ID que se pasa por la ruta
            y = ActorFilm.objects.filter(title = x) # busca en BBDD de ActorFilm el titulo que tenga ese ID que se pasa por la ruta

            data = []

            for actor in y:
                data.append({ # el append agrega un diccionario a data que es un array
                "Name": str(actor.actorName),
                "LastName": str(actor.actorName.actorLastName) # a traves de la ForeingKey
            })

            return JsonResponse({"title": str(actor.title), "actors": data}, safe=False, status=200)

        except Film.DoesNotExist:
            return JsonResponse({"error": "The movie with that title has not been found"}, status=404)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

# peliculas/<id>
# devuelve un json con los campos de title y actors, este ultimo es un array que tiene diccionarios con los campos de Name y LastName
# devuelve el json a traves de un ID que se escribe en la ruta

@csrf_exempt
def score_pelicula(request, id):
    if request.method == "POST":
        t = request.headers.get('token')

        if t != None:
            user = User.objects.get(tokenSesion=t)
            json_data = json.loads(request.body)

            score = json_data.get("score")

            pelicula = Film.objects.get(id=id)

            Score.objects.update_or_create(userName=user, film=pelicula, defaults={"filmScore":score})

            return JsonResponse({}, status=200)

        else:
            return JsonResponse({"error": "Token does not exits"}, status=401)
    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)