from django.db import models

class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, unique=True)
    alamat = models.CharField(max_length=255, blank=True)
    nomor_telepon = models.CharField(max_length=15, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='static/images/profil/', null=True, blank=True) 

    def __str__(self):
        return self.nama
