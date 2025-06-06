from django.shortcuts import get_object_or_404, render
from datetime import datetime

from sakila.models import Actor, Country, Film, User
from django.db.models import Q

def login(request):
    error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return render(request, 'banniere.html', {'hours': datetime.now().strftime("%Y-%m-%d - %H:%M:%S"), 'cname': username})
            else:
                error = True
        except User.DoesNotExist:
            error = True
    return render(request, 'login.html', {'form': {}, 'error': error})

def status(request):
    h = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
    cname = "Bradley"
    return render(request, 'banniere.html', {'hours': h, 'cname': cname})

def pays(request):
    pays = Country.objects.all()
    return render(request, 'liste_pays.html', {'pays': pays})


def films(request):
    query = request.GET.get('q', '')
    films = Film.objects.filter(title__icontains=query) if query else Film.objects.all()
    return render(request, 'films.html', {'films': films, 'query': query})

def actors(request):
    query = request.GET.get('q', '')
    actors = Actor.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query)
    ) if query else Actor.objects.all()
    return render(request, 'actors.html', {'actors': actors, 'query': query})

def film_detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    actors = film.actors.all()
    return render(request, 'film_detail.html', {'film': film, 'actors': actors})