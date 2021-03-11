from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Film, Director

def index(request):
    films = Film.objects.order_by('-date_upload')
    context = {'films': films}
    return render(request, 'index.html', context)

def film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    context = {'film': film}
    return render(request, 'film.html', context)

def director(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    context = {'director': director}
    return render(request, 'director.html', context)
