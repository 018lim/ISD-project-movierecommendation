from django.contrib import admin

# Register your models here.
from movies.models import UserInfo, Genre, MovieInfo, MovieRating, UserList

admin.site.register(UserInfo)
admin.site.register(Genre)
admin.site.register(MovieInfo)
admin.site.register(MovieRating)
admin.site.register(UserList)