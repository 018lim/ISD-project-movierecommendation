from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.if_else,name='if_else'),
    path('3/', views.for_loop, name='for_loop'),
    path('4/', views.ifequal_func, name='ifequal_function'),
    path('5/', views.filter_func, name = 'filter_function'),
    path('today/', views.today_is, name = 'today_is'),
    path('home/', views.home, name = 'home'),
    path('blog/',views.blog, name = 'blog'),
    path('tablecss/', views.index2, name='index2'),
    path('contact/',views.contact, name = 'contact'),
]