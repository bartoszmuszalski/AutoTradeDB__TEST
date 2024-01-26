from django import forms

from ogloszenia.models import ZamieszczanieOgloszen

class StworzFormularzOgloszenia(forms.ModelForm):

    class Meta:
        model = ZamieszczanieOgloszen
        fields = ['tytul', 'opis', 'cena', 'zdjecie', 'nrTelefonu', 'markaPojazdu', 'modelPojazdu', 'rokProdukcji', 'pojemnoscSilnika', 'typSilnika', 'lokalizacja']

class ZaaktalizujFormularzOgloszenia(forms.ModelForm):

    class Meta:
        model = ZamieszczanieOgloszen
        fields = ['tytul', 'opis', 'cena', 'zdjecie', 'nrTelefonu', 'markaPojazdu', 'modelPojazdu', 'rokProdukcji', 'pojemnoscSilnika', 'typSilnika', 'lokalizacja']

    def save(self, commit=True):
        zamieszczanie_ogloszen = self.instance
        zamieszczanie_ogloszen.tytul = self.cleaned_data['tytul']
        zamieszczanie_ogloszen.opis = self.cleaned_data['opis']
        zamieszczanie_ogloszen.cena = self.cleaned_data['cena']
        zamieszczanie_ogloszen.nrTelefonu = self.cleaned_data['nrTelefonu']      
        zamieszczanie_ogloszen.markaPojazdu = self.cleaned_data['markaPojazdu']
        zamieszczanie_ogloszen.modelPojazdu = self.cleaned_data['modelPojazdu']      
        zamieszczanie_ogloszen.rokProdukcji = self.cleaned_data['rokProdukcji']
        zamieszczanie_ogloszen.pojemnoscSilnika = self.cleaned_data['pojemnoscSilnika']      
        zamieszczanie_ogloszen.typSilnika = self.cleaned_data['typSilnika']
        zamieszczanie_ogloszen.lokalizacja = self.cleaned_data['lokalizacja']        

        if self.cleaned_data['zdjecie']:
            zamieszczanie_ogloszen.zdjecie = self.cleaned_data['zdjecie']
        
        if commit:
            zamieszczanie_ogloszen.save()

        return zamieszczanie_ogloszen
