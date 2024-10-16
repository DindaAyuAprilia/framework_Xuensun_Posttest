from django import forms
from .models import Penulis
from .models import Kategori

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']

class PenulisForm(forms.ModelForm):
    class Meta:
        model = Penulis
        fields = ['foto', 'nama_penulis', 'biodata', 'tanggal_lahir']
