from django.db import models
from xue.models.penulis import Penulis

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    id_buku = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=255, unique=True)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    tahun_terbit = models.IntegerField()
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    kategori = models.ManyToManyField(Kategori, related_name='buku')  
    gambar = models.ImageField(upload_to='static/images/cover/', null=True, blank=True)   # Field untuk menyimpan gambar

    def __str__(self):
        return self.judul