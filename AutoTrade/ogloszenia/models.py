from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

PATH_FOR_BRAND = 'C:\\Users\\barto\\Desktop\\Studia\\5sem\\AutoTradePROJECT\\AutoTrade\\ogloszenia\\static\\markiPojazdu.txt'

def upload_location(instance, filename, **kwargs):
    file_path = 'ogloszenia/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.autor.id), title=str(instance.tytul), filename=filename
        )
    return file_path


def read_choices_from_file(file_path):
    with open(file_path, 'r') as file:
        choices = [line.strip().split(' ', 1) for line in file]
    return choices

WYBOR_MARKI = read_choices_from_file(PATH_FOR_BRAND)

class ZamieszczanieOgloszen(models.Model):

    WYBOR_SILNIKA = [
        ('D', 'Diesel'),
        ('B', 'Benzyna'),
        ('E', 'Elektryk'),
        ('H', 'Hybryda'),
    ]

    STATUS_CHOICES = [
        ('oczekujace', 'Oczekujące na zatwierdzenie'),
        ('zatwierdzone', 'Zatwierdzone'),
    ]

    
    tytul               = models.CharField(max_length=50, null=False, blank=False)
    opis                = models.TextField(max_length=500, null=False, blank=False)
    cena                = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    autor               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zdjecie             = models.ImageField(upload_to=upload_location, null=False, blank=False)
    nrTelefonu          = models.CharField(max_length=15, null=False, blank=False)
    dataDodania         = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    dataAktualizacji    = models.DateTimeField(auto_now=True, verbose_name="Data aktualizacji")
    markaPojazdu        = models.CharField(max_length=50, choices=WYBOR_MARKI ,null=False, blank=False)
    modelPojazdu        = models.CharField(max_length=50, null=False, blank=False)
    rokProdukcji        = models.PositiveIntegerField(null=False, blank=False)
    pojemnoscSilnika    = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    typSilnika          = models.CharField(max_length=8, choices=WYBOR_SILNIKA, null=False, blank=False)
    lokalizacja         = models.CharField(max_length=50, null=False, blank=False)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.tytul
    
@receiver(post_delete, sender=ZamieszczanieOgloszen)
def UsunOgloszenie(sender, instance, **kwargs):
    instance.zdjecie.delete(False)

def ZapisPrzedZamieszczeniemOgloszenia(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.autor.username + "-" + instance.tytul)

pre_save.connect(ZapisPrzedZamieszczeniemOgloszenia, sender=ZamieszczanieOgloszen)
