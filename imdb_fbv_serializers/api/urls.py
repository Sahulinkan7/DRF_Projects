from django.urls import path
from . import views

urlpatterns = [
    path("movies/",views.movieapi),
    path("movies/id=<int:pk>",views.movie_update)
]
