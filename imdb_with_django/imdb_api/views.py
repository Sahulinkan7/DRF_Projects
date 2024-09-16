from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def getmovies(request):
    movies=Movie.objects.all()
    data={"name":list(movies.values())}
    return JsonResponse(data)


def get_movie(request,id):
    movie=Movie.objects.get(pk=id)
    data={"name":movie.name,
          "desc":movie.description,
          "active":movie.active}
    
    return JsonResponse(data)