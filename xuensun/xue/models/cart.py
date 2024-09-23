from django.db import models
from xue.models.buku import Buku
from xue.models.users import Users

class Cart(models.Model):
    id_keranjang = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=1)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.nama} - {self.buku.judul} ({self.jumlah})"
