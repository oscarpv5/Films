from django.http import JsonResponse
from appFilms.models import Film, Actor


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
            peliculas = Film.objects.filter(title__icontains=s)

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