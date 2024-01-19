from django.urls import path
from ogloszenia.views import(
    StworzWidokOgloszenia,
    SzczegolowyWidokOgloszewnia,
    EdytujWidokOgloszenia,
)

app_name = 'ogloszenia'

urlpatterns =[
    path('dodaj/', StworzWidokOgloszenia, name="dodaj"),
    path('<slug>/', SzczegolowyWidokOgloszewnia, name="szczegoly"),
    path('<slug>/edytuj', EdytujWidokOgloszenia, name="edytuj"),  
]