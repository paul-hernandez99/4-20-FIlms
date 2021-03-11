from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<int:film_id>', views.film, name='film'),
    path('director/<int:director_id>', views.director, name='director'),
]
