from django import forms

from . import models
from .models import MovieInfo, MovieRating, Genre


class MovieForm(forms.ModelForm):
    ne = forms.IntegerField()
    total_score = forms.FloatField()
    genre_id = forms.ModelChoiceField(queryset=Genre.objects.all())

    movie_title = forms.CharField(max_length=100)
    #poster = forms.ImageField(upload_to='posters')
    poster = forms.URLField()
    director = forms.CharField(max_length=100)
    cast = forms.CharField(max_length=200)

    class Meta:
        model = MovieInfo
        fields = ['movie_title','genre_id','poster','director','cast']



class RatingForm(forms.ModelForm):
    class Meta:
        model = MovieRating
        fields = ['score']