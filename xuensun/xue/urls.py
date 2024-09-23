<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name="homepage"),
path('detail_buku/', views.detail_buku, name="detail_buku"),

path('daftar_buku/', views.daftar_buku, name="daftar_buku"),
=======
from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name="homepage"),
path('detail_buku/', views.detail_buku, name="detail_buku"),

path('daftar_buku/', views.daftar_buku, name="daftar_buku"),
>>>>>>> 4ba49aabbb0e6db88f230316516cc65a0e4639a3
]