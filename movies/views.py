from django.shortcuts import render, get_object_or_404, redirect
from .movieform import MovieForm, RatingForm
from .models import MovieInfo, MovieRating, Genre
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, update_session_auth_hash

from django.template.defaulttags import register

from django.db.models import Avg

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RatingSerializer



#
def create(request):
    # superuser?
    if request.user.is_superuser:
        if request.method == "POST":
            form = MovieForm(request, request.FILES)
            if form.is_valid():
                movie = form.save()
                # if superuser go to movie-detail
                return render(request, 'movies/moviedetail.html', movie)
            else:
                return render(request, 'error.html')

        else:
            form = MovieForm()
        return render(request, 'movies/create.html', {'form': form})

    else:
        return redirect('movies:list')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)





def detail(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    ratings = MovieRating.objects.filter(movie_id=movie_id)
    #rated = MovieRating.objects.get(score=-1)

    for rating in ratings:
        if request.user == rating.user:
            rated = rating
    rating_form = RatingForm()

    print(ratings.values())

    sum = MovieRating.objects.filter(movie_id=movie_id).aggregate(Avg('score'))
    if sum['score__avg']:
        avg_score = round(sum['score__avg'], 2)
    else:
        avg_score = 0

    anScore=movie.total_score/movie.ne
    context = {
        'movie': movie,
        'rating_form': rating_form,
        'ratings': ratings,
        'avg_score': avg_score,
        'anScore': anScore,
        #'rated': rated
    }

    return render(request, 'movies/detail.html', context)


def update(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)

    if not request.user.is_superuser:
        return redirect('movies:list')

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = MovieForm(instance=movie)
        return render(request, 'movies/update.html', {'form': form})


@require_POST
def delete(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    if request.user.is_superuser:
        movie.delete()
    return redirect('movies:list')



@login_required
def create_rating(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    form = RatingForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)

        rating.user = request.user
        rating.movie = movie
        rating.save()

    return redirect('movies:detail', movie.id)


@api_view(['POST', 'GET'])
def starcreate_rating(request, movie_id):
    rating = request.data
    serializer = RatingSerializer(data=rating)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@require_POST
def delete_rating(request, movie_id, rating_id):
    rating = MovieRating.objects.get(pk=rating_id)
    if rating.user == request.user:
        rating.delete()
    return redirect('movies:detail', movie_id)


@login_required
def update_rating(request, movie_id, rating_id):
    rating = MovieRating.objects.get(pk=rating_id)
    if rating.user == request.user:
        if request.method == "POST":
            form = RatingForm(request.POST, instance=rating)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_id)
        else:
            form = RatingForm(instance=rating)
        return render(request, 'movies/update.html', {'form': form})

    else:
        return redirect('movies:list')





def recommend(request):
    return render(request, 'movies/recommend.html')





def start(request):
    return render(request, 'movies/start.html')

#to import info from API
import urllib.request, json

def list_genres(request):
    with urllib.request.urlopen(
            "https://api.themoviedb.org/3/genre/movie/list?api_key=459cfe259d40ef74b24fa3f9a19c6f3a&language=en-US") as url:
        data = json.loads(url.read().decode())

    genres = Genre.objects.all()
    genresList = list(genres)

    for i in data["genres"]:
        save = 0
        for j in genresList:
            if j.genre_name == i['name']:
                save = 1
        if save == 1:
            print("sista")
        else:
            print("proceso para añadir dato")
            new = Genre(genre_name=i['name'])
            new.save()

    context = {
        'genres': genres,
        'DBgenres': data,
    }

    return render(request, 'viewFeed.html', context)

def movies_list(request):
    #change the number of the list

    with urllib.request.urlopen(
            "https://api.themoviedb.org/3/genre/movie/list?api_key=459cfe259d40ef74b24fa3f9a19c6f3a&language=en-US") as url:
        genresDB = json.loads(url.read().decode())

    genres = Genre.objects.all()
    genresList = list(genres)

    movies=MovieInfo.objects.all()
    moviesList=list(movies)

    for lists in [1,2,3,4,5,6,7]:
        with urllib.request.urlopen(
                "https://api.themoviedb.org/3/list/"+str(lists)+"?api_key=459cfe259d40ef74b24fa3f9a19c6f3a&language=en-US") as url:
            data = json.loads(url.read().decode())

        for i in data["items"]:
            itExist=0

            for j in moviesList:
                if i["id"] == j.idTMDB:
                    itExist=1

            if itExist == 0:
                for j in genresDB["genres"]:
                    if i["genre_ids"][0] == j['id']:
                        for k in genresList:
                            if k.genre_name == j['name']: #if the genre exists in our database

                                nE=i['vote_count']
                                totalScore=i['vote_average']*nE
                                idTMDBb=i["id"]
                                movieTitle=i['original_title']

                                with urllib.request.urlopen(
                                        "https://api.themoviedb.org/3/movie/"+str(i['id'])+"/credits?api_key=459cfe259d40ef74b24fa3f9a19c6f3a&language=en-US") as url:
                                    movieDetail = json.loads(url.read().decode())

                                cast = ''
                                num=0
                                for r in movieDetail['cast']:
                                    if r['known_for_department'] == "Acting":
                                        if num == 0:
                                            cast=cast+r['name']
                                        else:
                                            cast = cast + ',' + r['name']
                                        num=num+1
                                print(cast) #add cast

                                direct=''
                                num=0
                                for r in movieDetail['crew']:
                                    if r['job'] == "Director":
                                        if num == 0:
                                            direct=direct+r['name']
                                        else:
                                            direct = direct + ',' + r['name']
                                        num=num+1
                                print(direct)  # add director

                                poster='https://image.tmdb.org/t/p/w500'+i['poster_path']

                                new = MovieInfo(ne = nE, total_score=totalScore, movie_title=movieTitle, poster=poster, director=direct, cast=cast, genre_id_id=k.pk, idTMDB=idTMDBb)
                                new.save()
            else:
                print("ya hay peli")
                print(i["genre_ids"][0])

    context = {
        'DBmovies': data["items"],
    }

    return render(request, 'viewFeed.html', context)

def D1_page(request):
    context = {
        'Data': 0,
    }
    return render(request, 'movies/detail_D1.html', context)
