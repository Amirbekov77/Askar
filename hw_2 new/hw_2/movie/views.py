from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().values('id', 'title', 'description', 'producer', 'duration')
    return JsonResponse(list(movies), safe=False)

def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = {
            'title': movie.title,
            'description': movie.description,
            'producer': movie.producer,
            'duration': movie.duration
        }
        return JsonResponse(data)
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
