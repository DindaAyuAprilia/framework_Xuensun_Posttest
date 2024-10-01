from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.utils.html import format_html  # Import untuk menampilkan HTML
from .models.admin import Admin
from .models.akun import Akun
from .models.users import Users
from .models.penulis import Penulis
from .models.buku import Buku
from .models.kategori import Kategori
from .models.cart import Cart

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id_admin', 'nama_admin', 'email', 'nomor_telepon')
    search_fields = ('nama_admin', 'email')

    def save_model(self, request, obj, form, change):
        # Simpan objek Admin terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah Akun dengan email Admin sudah ada
        akun, created = Akun.objects.get_or_create(
            email=obj.email,
            defaults={
                'password': make_password('123'),  # Ganti dengan password yang sesuai
                'role': Akun.ADMIN,
            }
        )

        if not created:
            # Jika Akun sudah ada, perbarui peran dan password jika diperlukan
            akun.role = Akun.ADMIN
            akun.password = make_password('default_password')  # Opsional: Hanya jika ingin memperbarui password
            akun.save()

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'nama', 'email', 'nomor_telepon', 'tanggal_lahir', 'alamat', 'foto_thumbnail')
    search_fields = ('nama', 'email', 'alamat')  # Menambahkan 'alamat' ke dalam pencarian

    def save_model(self, request, obj, form, change):
        # Simpan objek Users terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah Akun dengan email Users sudah ada
        akun, created = Akun.objects.get_or_create(
            email=obj.email,
            defaults={
                'password': make_password('default_password'),  # Ganti dengan password yang sesuai
                'role': Akun.USERS,
            }
        )

        if not created:
            # Jika Akun sudah ada, perbarui peran dan password jika diperlukan
            akun.role = Akun.USERS
            akun.password = make_password('default_password')  # Opsional: Hanya jika ingin memperbarui password
            akun.save()

    def foto_thumbnail(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.foto.url)
        return '-'
    foto_thumbnail.short_description = 'Foto'  # Nama kolom di admin

class AkunAdmin(admin.ModelAdmin):
    list_display = ('email', 'get_role_display')
    search_fields = ('email', 'role')

    def get_role_display(self, obj):
        return obj.get_role_display()
    get_role_display.short_description = 'Role'
    
class PenulisAdmin(admin.ModelAdmin):
    list_display = ('id_penulis', 'nama_penulis', 'tanggal_lahir', 'foto_thumbnail')
    search_fields = ('nama_penulis', 'biodata')

    def foto_thumbnail(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />',
                obj.foto.url
            )
        return '-'
    foto_thumbnail.short_description = 'Foto Penulis'

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama')
    search_fields = ('nama',)
    
class BukuAdmin(admin.ModelAdmin):
    list_display = ('id_buku', 'judul', 'harga', 'tahun_terbit', 'penulis', 'kategori_list', 'gambar_thumbnail')
    search_fields = ('judul', 'deskripsi', 'penulis__nama_penulis')
    list_filter = ('kategori', 'penulis')

    filter_horizontal = ('kategori',)  # Menampilkan widget horizontal untuk ManyToManyField

    def kategori_list(self, obj):
        return ", ".join([kategori.nama for kategori in obj.kategori.all()])
    kategori_list.short_description = 'Kategori'

    def gambar_thumbnail(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.gambar.url
            )
        return '-'
    gambar_thumbnail.short_description = 'Gambar Buku'


class CartAdmin(admin.ModelAdmin):
    list_display = ('id_keranjang', 'user', 'buku', 'jumlah', 'tanggal_ditambahkan')
    search_fields = ('user__nama', 'buku__judul')

# Daftarkan Model dengan kelas Admin khusus
admin.site.register(Admin, AdminAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Akun, AkunAdmin)
admin.site.register(Penulis, PenulisAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Buku, BukuAdmin)
admin.site.register(Cart, CartAdmin)

