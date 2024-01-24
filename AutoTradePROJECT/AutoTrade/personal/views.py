from django.shortcuts import render
from operator import attrgetter
from ogloszenia.models import ZamieszczanieOgloszen
from ogloszenia.views import get_blog_queryset
# Create your views here.

def home_screen_view(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)


    #Sortuje od najnowszych


    zamieszczanie_ogloszen = sorted(get_blog_queryset(query), key=attrgetter('tytul'), reverse=True)
    context['zamieszczanie_ogloszen'] = zamieszczanie_ogloszen

    return render(request,"personal/home.html", context)

