from django.urls import path
from . import views

urlpatterns = [
    path("movies/",views.getmovies),
    path("movie/<int:id>",views.get_movie)
]
