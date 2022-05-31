from django.urls import path

from snacks import views

urlpatterns = [
    path('', views.list_snacks, name = 'list_snacks'),
    path('new/',views.create_snack,name='add_snack'),
    path('update/<int:id>/', views.update_snack, name = 'update_snack'),
    path('delete/<int:id>/', views.delete_snack, name = 'delete_snack'),
]