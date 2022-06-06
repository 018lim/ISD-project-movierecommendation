from django.urls import path, include

import movies
from . import views
#from .views import viewfeed

app_name = "movies"

urlpatterns = [
    #path('', views.list_genres),
    path('upGenres/', views.list_genres),
    path('upMovies/', views.movies_list),
    path('D1/', views.D1_page,name="D1"),
    path('Genre/<int:genre_id>/', views.byGenre),
    path('search/', views.search, name="search"),

    #path('', views.list, name="list"),







]

