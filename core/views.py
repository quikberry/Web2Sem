from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.db.models import Count, Avg
from .models import Movie, Session, Review

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'core/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'core/movie_detail.html', {'movie': movie})

def index(request):
        #Ближайшие релизы
    upcoming_movies = Movie.objects.filter().order_by('created_at')[:5]

    #Частопосещаемые
    popular_by_sessions = Movie.objects.annotate(
        session_count=Count('session')
    ).order_by('-session_count')[:5]

    #Лучшие по оценкам
    top_rated = Movie.objects.annotate(
        avg_rating=Avg('review__rating')
    ).filter(avg_rating__isnull=False).order_by('-avg_rating')[:5]

    context = {
        'upcoming_movies': upcoming_movies,
        'popular_by_sessions': popular_by_sessions,
        'top_rated': top_rated,
    }
    return render(request, 'core/index.html', context)