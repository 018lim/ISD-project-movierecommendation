from django import forms
from .models import Movie, Rating


class MovieForm(forms.ModelForm):
    ne = models.IntegerField()
    total_score = models.FloatField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie_title = forms.CharField(max_length=100)
    poster = forms.ImageField(upload_to='posters')
    director = forms.CharField(max_length=100)
    cast = fomrs.CharField(max_length=200)

    class Meta:
        field = ['movie_title','ne','total_score','genre_id','poster','director','cast']






class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']