from django import forms
from .models import MovieInfo, MovieRating


class SearchForm(forms.ModelForm):
    word = forms.CharField(label="Movie Name", max_length=30)


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'
