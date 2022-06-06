from rest_framework import serializers
from .models import MovieRating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ['id','genre','score','user','movie']
