from django.shortcuts import render

# Create your views here.
@login_required
def create_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.movie = movie
        rating.save()
    # 다음에 다시 상세페이지로 보내기
    return redirect('movies:detail', movie.id)


@api_view(['POST', 'GET'])  # 허용할 http method를 적어줌
def starcreate_rating(request, movie_id):
    rating = request.data
    serializer = RatingSerializer(data=rating)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@require_POST
def delete_rating(request, movie_id, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if rating.user == request.user:
        rating.delete()
    return redirect('movies:detail', movie_id)


@login_required
def update_rating(request, movie_id, rating_id):
    rating = Rating.objects.get(pk=rating_id)
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
