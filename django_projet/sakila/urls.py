from django.urls import path
from sakila.views import actors, film_detail, films, pays, status, login

urlpatterns = [
    path('', login, name='login'),
    path('accueil/', status, name='banniere'),
    path('pays/', pays, name='liste_pays'),
    path('films/', films, name='films'),
    path('actors/', actors, name='actors'),
    path('films/<int:film_id>/', film_detail, name='film_detail'),
]