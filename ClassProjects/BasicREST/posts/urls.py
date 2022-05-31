from django.urls import path

from . import views
from .views import jsonview, viewfeed, viewjson, viewrest


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('jsonview/', jsonview, name = 'jsonview'),
    path('viewfeed/', viewfeed, name = 'viewfeed'),
    path('viewjson/', viewjson, name = 'viewjson'),
    path('viewrest/', viewrest, name = 'viewrest'),
    path('viewbar', views.viewbar, name = 'viewbar'),
    path('viewbubble', views.viewbubble, name='viewbubble'),
    path('viewpie', views.viewpie, name='viewpie'),
    path('viewdynamic', views.viewdynamic, name='viewdynamic'),
    path('viewmultiple', views.viewmultiple, name='viewmultiple'),
    path('viewmap', views.viewmap, name='viewmap'),
    path('viewgeo', views.viewgeo, name='viewgeo'),

]