import json
from datetime import datetime

from django.http import JsonResponse
from appFilms.models import Film, Actor
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


def prueba1(request):
    return JsonResponse({})

def prueba2(request, valor1, valor2):
    return JsonResponse(
        {
            "Estado": valor1,
            "Nuevo estado": valor2
        })

def prueba3(request, valor):
    return JsonResponse({"Estado": valor})

def prueba4(request, valor):
    return JsonResponse({"Estado": valor})

def prueba5(request):
    if request.method == "GET":
        q = request.GET.get('q')
        print(f"Query param q: {q}")
        return JsonResponse({'query': q})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def prueba6(request, valor):
    if request.method == "GET":
        q = request.GET.get('q')
        print(f"Query param q: {q}")
        return JsonResponse({'valor': valor, 'query': q})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def prueba7(request):
    if request.method == "GET":
        q = request.GET.get('q')
        p = request.GET.get('p')
        print(f"q = {q}, p = {p}")
        return JsonResponse({'q': q, 'p': p})

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def titulo(request, title):
    if request.method == "GET":
        try:
            x = Film.objects.get(title=title)
            return JsonResponse({
                "title": x.title
            })
        except Film.DoesNotExist:
            return JsonResponse({"error": "The movie with that title has not been found"}, status=404)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def peliculas(request):
    if request.method == "GET":

        s = request.GET.get("search")

        if s is None:
            peliculas = Film.objects.all()
        else:
            peliculas = Film.objects.filter(Q(title__icontains=s) | Q(synopsis__icontains=s))

        data = []
        for pelicula in peliculas:
            data.append({
                "Id": pelicula.id,
                "Title": pelicula.title,
                "Synopsis": pelicula.synopsis,
                "Year": pelicula.year
            })
        return JsonResponse(data, safe=False, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

def actores(request):
    if request.method == "GET":
        actores = Actor.objects.all()

        data = [{
            "Id": actor.id,
            "Name": actor.actorName,
            "Last name": actor.actorLastName,
            "Gender": actor.gender
        } for actor in actores]

        return JsonResponse(data, safe=False, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)

@csrf_exempt
def usuarios(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)

        return JsonResponse({}, status=200)

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

            usuario = json_data["username"]
            contrasena = json_data["password"]

            print("Usuario: " + usuario)
            print("Contraseña: " + contrasena)

        except KeyError:
            return JsonResponse({"error": "Missing user and/or password"}, status=400)

        return JsonResponse({}, status=200)

    else:
        return JsonResponse({"error": "HTTP method not supported"}, status=405)