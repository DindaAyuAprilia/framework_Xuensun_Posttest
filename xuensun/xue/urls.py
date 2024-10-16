from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('detail_buku/', views.detail_buku, name="detail_buku"),
    #############################################################
    path('penulis/', views.penulis_index, name='penulis_index'),
    path('penulis/create/', views.penulis_create, name='penulis_create'),
    path('penulis/update/<int:penulis_id>/', views.penulis_update, name='penulis_update'),
    path('penulis/delete/<int:id_penulis>/', views.penulis_delete, name='penulis_delete'),
    #############################################################
    path('kategori/', views.kategori_index, name='kategori_index'),
    path('kategori/create/', views.kategori_create, name='kategori_create'),
    path('kategori/update/<int:kategori_id>/', views.kategori_update, name='kategori_update'),
    path('kategori/delete/<int:kategori_id>/', views.kategori_delete, name='kategori_delete'),
    path('daftar_buku/', views.daftar_buku, name="daftar_buku"),
]