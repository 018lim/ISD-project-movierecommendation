"""ISD_project_movierecommendation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upGenres/', views.list_genres),
    path('upMovies/', views.movies_list),
    path('D1/', views.D1_page,name="D1"),
    path('D2/<int:movie_id>/', views.D2_page,name="D2"),
    path('Genre/<int:genre_id>/', views.byGenre),
    path('search/', views.search, name="search"),
    path('movies/', include('movies.urls', namespace="namespace")),
    path('movieList/', views.moviesList, name="create"),
    #path('', views.list, name="list"),

    path('vizTest/', views.vizTest, name = 'vizTest'),
    path('searchMovieViz/', views.searchMovieViz, name = 'vizTest'),
    path('searchMovieTitles/', views.searchMovieTitles, name = 'vizTestTitles'),
    path('searchMovieMain/', views.searchMovieMain, name = 'vizTestMain'),


    #path('<int:movie_id>/', views.detail, name="detail"),



    #path('', views.py, name = 'index'),

]
