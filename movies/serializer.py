from rest_framework import serializers
#from .models import Rating

from .models import MovieRating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ['movie_id', 'score']
