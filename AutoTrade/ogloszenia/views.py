from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from ogloszenia.models import ZamieszczanieOgloszen
from ogloszenia.forms import StworzFormularzOgloszenia, ZaaktalizujFormularzOgloszenia
from account.models import Account
from django.db.models import Q
from django.http import HttpResponse

def StworzWidokOgloszenia(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form = StworzFormularzOgloszenia(request.POST or None, request.FILES or None)
    # print(f'Title: {}, Content: {content}')
    if form.is_valid():
        # print(form)
        obj = form.save(commit=False)
        autor = Account.objects.filter(email=user.email).first()
        obj.autor = autor
        obj.save()
        form = StworzFormularzOgloszenia

    context['form'] = form

    return render(request, "ogloszenia/dodaj_ogloszenie.html", context)

def SzczegolowyWidokOgloszewnia(request, slug):
    context = {}

    zamieszczanie_ogloszen = get_object_or_404(ZamieszczanieOgloszen, slug=slug)
    context['zamieszczanie_ogloszen'] = zamieszczanie_ogloszen

    return render(request, 'ogloszenia/szczegoly_ogloszenia.html', context)

def EdytujWidokOgloszenia(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    zamieszczanie_ogloszen = get_object_or_404(ZamieszczanieOgloszen, slug=slug)

    if zamieszczanie_ogloszen.autor != user:
        return HttpResponse('Nie jesteś autorem tego ogłoszenia.')
    
    if request.POST:
        form = ZaaktalizujFormularzOgloszenia(request.POST or None, request.FILES or None, instance=zamieszczanie_ogloszen)
        if form.is_valid():
            print("s")
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Zaaktulizwano"
            zamieszczanie_ogloszen = obj
        else:
            print("OK")
    form = ZaaktalizujFormularzOgloszenia(
            initial = {
                "tytul": zamieszczanie_ogloszen.tytul,
                "zdjecie": zamieszczanie_ogloszen.zdjecie,
                "opis": zamieszczanie_ogloszen.opis,
                "cena": zamieszczanie_ogloszen.cena,
                "nrTelefonu": zamieszczanie_ogloszen.nrTelefonu,
                "markaPojazdu": zamieszczanie_ogloszen.markaPojazdu,
                "modelPojazdu": zamieszczanie_ogloszen.modelPojazdu,
                "rokProdukcji": zamieszczanie_ogloszen.rokProdukcji,
                "pojemnoscSilnika": zamieszczanie_ogloszen.pojemnoscSilnika,
                "typSilnika": zamieszczanie_ogloszen.typSilnika,
                "lokalizacja": zamieszczanie_ogloszen.lokalizacja,
            }
        )

    context['form'] = form
    return render(request, 'ogloszenia/edytuj_ogloszenie.html', context)

def UsunWidokOgloszenia(request, slug):
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('must_authenticate')

    zamieszczanie_ogloszen = get_object_or_404(ZamieszczanieOgloszen, slug=slug)

    if zamieszczanie_ogloszen.autor != user:
        return HttpResponse('Nie jesteś autorem tego ogłoszenia.')

    if request.method == 'POST':
        # Jeśli formularz został przesłany
        zamieszczanie_ogloszen.delete()
        return redirect('must_authenticate')

    context['zamieszczanie_ogloszen'] = zamieszczanie_ogloszen
    return render(request, 'ogloszenia/usun_ogloszenie.html', context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ") # rozdziela to na liste czyli ['ford', 'bravo', itptitp]
    for q in queries:
        ogloszenia = ZamieszczanieOgloszen.objects.filter(
                                                        Q(tytul__icontains=q) |
                                                        Q(opis__icontains=q)
                                                        ).distinct()
        for ogloszenie in ogloszenia:
            queryset.append(ogloszenie)
    return list(set(queryset))
