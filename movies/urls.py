from django.urls import path

from . import views
#from .views import viewfeed


urlpatterns = [
    #path('', views.list_genres),
    path('upGenres/', views.list_genres),
    path('upMovies/', views.movies_list),
    path('detail/<int:movie_id>', views.detail),
    path('D1/', views.D1_page),
]
