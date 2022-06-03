from django.urls import path

from . import views
#from .views import viewfeed


urlpatterns = [
    path('', views.list_genres),
    path('upDB/', views.list_genres),
]