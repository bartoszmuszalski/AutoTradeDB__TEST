from django.urls import path
from ogloszenia.views import(
    StworzWidokOgloszenia,
    SzczegolowyWidokOgloszewnia,
    EdytujWidokOgloszenia,
    UsunWidokOgloszenia,
)

app_name = 'ogloszenia'

urlpatterns =[
    path('dodaj/', StworzWidokOgloszenia, name="dodaj"),
    path('<slug>/', SzczegolowyWidokOgloszewnia, name="szczegoly"),
    path('<slug>/edytuj', EdytujWidokOgloszenia, name="edytuj"),
    path('<slug>/usun', UsunWidokOgloszenia, name="usun"),
]