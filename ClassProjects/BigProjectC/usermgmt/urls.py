from django.urls import path

from usermgmt import views

urlpatterns = [
    path('', views.list_members, name = 'list_members'),
    path('new/', views.create_member, name = 'add_member'),
    path('update/<int:id>/', views.update_member, name = 'update_member'),
    path('delete/<int:id>/', views.delete_member, name = 'delete_member'),
]
