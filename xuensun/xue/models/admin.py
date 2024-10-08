from django.db import models

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nama_admin = models.CharField(max_length=255, unique=True)
    nomor_telepon = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nama_admin
