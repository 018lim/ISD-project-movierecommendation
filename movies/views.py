from django.shortcuts import render, get_object_or_404, redirect
from .movieform import MovieForm, RatingForm
from .models import MovieInfo, MovieRating, Genre, UserInfo, UserList
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth import get_user_model, update_session_auth_hash

from django.template.defaulttags import register
from django.template import loader


from django.db.models import Avg

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RatingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.














def search(request):
    movie = MovieInfo.objects.all()
    # GET request의 인자중에 searchword값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if request.method == "GET":
        searchword = request.GET.get('searchword', '')
        resultMovie = []

        if searchword:  # searchword가 있다면
            searchMovie = movie.filter(title__contains=searchword)  # 제목에 searchword가 포함된 레코드만 필터링
            if searchMovie:
                # 영화 여러개 저장위해 데이터의 개수
                movie_count = searchMovie.count()
                for c in range(movie_count):
                    # 데이터들 resultMovie리스트에 저장
                    # 원본 주석처리
                    # resultMovie.append({searchMovie[c].title:searchMovie[c].id})
                    resultMovie.append({'title': searchMovie[c].title, 'id': searchMovie[c].id})
                    # 디테일 페이지 이동위해 id값도 넘겨준다
                return render(request, 'movies/searchresult.html',
                              {'movie': movie, 'searchMovie': searchMovie, 'resultMovie': resultMovie})
            else:
                # 아무것도 입력하지 않는다면,
                return render(request, 'movies/searchresult.html', {'resultMovie': resultMovie})

        return render(request, 'movies/search.html')

def moviesList(request):
    genres = Genre.objects.all()
    movies_form = MovieForm()
    movies = MovieInfo.objects.all()

    context={
        'genres':genres,
        'movies_form' : movies_form,
        'moviesList':movies,
    }


    return render(request, 'movies/moviesList.html', context=context)


def createF(request):
    user = UserInfo(userID=request.POST['userID'], user_pass=request.POST['pass'], user_name=request.POST['name'], user_email=request.POST['email'], is_superuser=['superUser'])
    user.save()
    userList = UserList(pref_genre='', nonpref_genre='', movie_list='', user_index_id=user.pk)
    userList.save()
    return render(request, 'crud/create.html')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Create your views here.









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

    moviesInfo=MovieInfo.objects.all()
    movies=list(moviesInfo)

    genres=Genre.objects.all()

    moviesList=[]
    for j in [2,3,4,5,6]:
        moviesList.append(movies[j])



    context = {
        'data': moviesList,
        'genres': genres,
    }
    return render(request, 'movies/detail_D1.html', context)

def D2_page(request, movie_id):
    movieInfo = MovieInfo.objects.get(id=movie_id)
    genre = movieInfo.genre_id.genre_name
    score=movieInfo.total_score/movieInfo.ne

    genres = Genre.objects.all()

    context = {
        'movie':movieInfo,
        'genre': genre,
        'score': score,
        'genres': genres,
    }

    return render(request, 'movies/D2.html', context)

def byGenre(request, genre_id):
    movieInfo = MovieInfo.objects.filter(genre_id=genre_id)
    genre = Genre.objects.get(id=genre_id).genre_name

    genres = Genre.objects.all()

    context = {
        'movies':movieInfo,
        'genre': genre,
        'genres': genres,
    }

    return render(request, 'movies/byGenre.html', context)

from django.shortcuts import render

def vizTest(request):
    temp = loader.get_template('movies/comparison.html')
    moviesInfo = MovieInfo.objects.all()
    movies = list(moviesInfo)

    genres = Genre.objects.all()

    moviesList = []
    for j in [2, 3, 4, 5, 6]:
        moviesList.append(movies[j])

    context = {
        'data': moviesList,
        'genres': genres,
    }
    return HttpResponse(temp.render(context, request))

def searchMovieViz(request):

    movie = MovieInfo.objects.get(movie_title=request.POST['movie'])
    title=movie.movie_title
    score=movie.total_score/movie.ne
    return JsonResponse({"title": title,"score": score}, status=200)

def searchMovieTitles(request):

    movie = list(MovieInfo.objects.filter(movie_title__startswith=request.POST['movie']).values_list('movie_title', flat=True))

    return JsonResponse({"titles": movie}, status=200)

def searchMovieMain(request):

    movie = MovieInfo.objects.filter(movie_title=request.POST['movie'])[:1].get().id
    return JsonResponse({"id": movie}, status=200)

