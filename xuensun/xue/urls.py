from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name="homepage"),
path('detail_buku/', views.detail_buku, name="detail_buku"),

path('daftar_buku/', views.daftar_buku, name="daftar_buku"),
]