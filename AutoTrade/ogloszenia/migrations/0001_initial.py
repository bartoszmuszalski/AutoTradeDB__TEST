# Generated by Django 5.0.1 on 2024-01-11 15:26

import django.db.models.deletion
import ogloszenia.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ZamieszczanieOgloszen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=50)),
                ('opis', models.TextField(max_length=500)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zdjecie', models.ImageField(upload_to=ogloszenia.models.upload_location)),
                ('nrTelefonu', models.CharField(max_length=15)),
                ('dataDodania', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('markaPojazdu', models.CharField(max_length=50)),
                ('modelPojazdu', models.CharField(max_length=50)),
                ('rokProdukcji', models.PositiveIntegerField()),
                ('pojemnoscSilnika', models.DecimalField(decimal_places=2, max_digits=5)),
                ('typSilnika', models.CharField(choices=[('D', 'Diesel'), ('B', 'Benzyna'), ('E', 'Elektryk'), ('H', 'Hybryda')], max_length=8)),
                ('lokalizacja', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
