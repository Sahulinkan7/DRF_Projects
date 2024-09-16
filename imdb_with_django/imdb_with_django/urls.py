
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("imdb_api/",include("imdb_api.urls"))
]
