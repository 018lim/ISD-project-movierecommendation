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
from django.urls import path

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upGenres/', views.list_genres),
    path('upMovies/', views.movies_list),
    path('D1/', views.D1_page,name="D1"),

    path('create/', views.create, name="create"),

    path('movieList/', views.moviesList, name="create"),
    #path('', views.list, name="list"),

    path('<int:movie_id>/', views.detail, name="detail"),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),

    path('<int:movie_id>/rating/create/', views.create_rating, name='create_rating'),
    path('<int:movie_id>/rating/<int:rating_id>/delete', views.delete_rating, name="delete_rating"),
    path('<int:movie_id>/rating/<int:rating_id>/update', views.update_rating, name="update_rating"),

    path('createUser/', views.create, name=""),
    #path('', views.py, name = 'index'),

]
