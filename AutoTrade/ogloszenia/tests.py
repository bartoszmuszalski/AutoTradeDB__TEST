from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ZamieszczanieOgloszen

class OgloszeniaTesty(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.ogloszenie = ZamieszczanieOgloszen.objects.create(
            autor=self.user,
            tytul='Testowy Tytuł',
            opis='Testowy Opis',
            cena=100,
            nrTelefonu='123456789',
            markaPojazdu='Testowa Marka',
            modelPojazdu='Testowy Model',
            rokProdukcji=2022,
            pojemnoscSilnika='2.0',
            typSilnika='Benzyna',
            lokalizacja='Testowa Lokalizacja',
        )

    def test_tworz_widok_ogloszenia(self):
        response = self.client.post(reverse('ogloszenia:dodaj'), {
            'tytul': 'Nowy Ogłoszenie',
            'opis': 'Opis nowego ogłoszenia',
            'cena': 200,
        })

        self.assertEqual(response.status_code, 302)  # Oczekujemy przekierowania (302)

        nowe_ogloszenie = ZamieszczanieOgloszen.objects.get(tytul='Nowy Ogłoszenie')
        self.assertEqual(nowe_ogloszenie.autor, self.user)

    def test_edytuj_widok_ogloszenia(self):
        response = self.client.post(reverse('ogloszenia:edytuj', args=[self.ogloszenie.slug]), {
            'tytul': 'Zaktualizowany Tytuł',
            'opis': 'Zaktualizowany Opis',
            'cena': 150,
        })

        self.assertEqual(response.status_code, 302)  # Oczekujemy przekierowania (302)

        self.ogloszenie.refresh_from_db()
        self.assertEqual(self.ogloszenie.tytul, 'Zaktualizowany Tytuł')

    def test_usun_widok_ogloszenia(self):
        response = self.client.post(reverse('ogloszenia:usun', args=[self.ogloszenie.slug]))

        self.assertEqual(response.status_code, 302)  # Oczekujemy przekierowania (302)
        with self.assertRaises(ZamieszczanieOgloszen.DoesNotExist):
            ZamieszczanieOgloszen.objects.get(slug=self.ogloszenie.slug)