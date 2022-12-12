from django.shortcuts import render
from .models import Director, Peliculas
# Create your views here.


def index(request):
    num_directores = Director.objects.all().count()
    num_peliculas = Peliculas.objects.all().count()

    return render(
        request,
        "index.htm",
        contex={
            'num_directores': num_directores,
            "num_peliculas": num_peliculas,
        }
    )
