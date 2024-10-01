from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama