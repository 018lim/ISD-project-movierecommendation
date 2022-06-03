from django.db import models


# Create your models here.

class UserInfo(models.Model):
    #user_index = models.IntegerField(unique=True)
    userID = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)

    # def __str__(self):
    #    return self.userID


class Genre(models.Model):
    #genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)


class MovieInfo(models.Model):
    #movie_id = models.IntegerField(unique=True)
    ne = models.IntegerField()
    total_score = models.FloatField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=100)
    poster = models.URLField('URL', unique=True)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=200)


class MovieRating(models.Model):
    score = models.FloatField()
    movie_id = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class UserList(models.Model):
    user_index = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    pref_genre = models.CharField(max_length=200)
    nonpref_genre = models.CharField(max_length=200)
    movie_list = models.CharField(max_length=200)
