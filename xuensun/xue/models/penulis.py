from django.db import models

class Penulis(models.Model):
    id_penulis = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='static/images/penulis/', null=True, blank=True) 
    nama_penulis = models.CharField(max_length=255)
    biodata = models.TextField()
    tanggal_lahir = models.DateField()

    def __str__(self):
        return self.nama_penulis
