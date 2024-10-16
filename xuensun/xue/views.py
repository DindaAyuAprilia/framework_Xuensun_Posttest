from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Penulis
from .forms import PenulisForm
from .models import Kategori
from .forms import KategoriForm

# CREATE Kategori
def kategori_create(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil ditambahkan!')
            return redirect('kategori_index')
        else:
            print(form.errors)
    else:
        form = KategoriForm()
    return render(request, 'kategori/create.html', {'form': form})

# READ Kategori (Index)
def kategori_index(request):
    query = request.GET.get('q')
    kategori_list = Kategori.objects.all()
    if query:
        kategori_list = Kategori.objects.filter(
            Q(nama__icontains=query)
        ).distinct()
    return render(request, 'kategori/index.html', {'kategori_list': kategori_list, 'query': query})

# UPDATE Kategori
def kategori_update(request, kategori_id):
    kategori = get_object_or_404(Kategori, id=kategori_id)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kategori berhasil diubah!')
            return redirect('kategori_index')
        else:
            messages.error(request, 'Terjadi kesalahan saat mengubah data kategori.')
    else:
        form = KategoriForm(instance=kategori)
    return render(request, 'kategori/update.html', {'form': form, 'kategori': kategori})

# DELETE Kategori
def kategori_delete(request, kategori_id):
    if request.method == 'POST':
        kategori = get_object_or_404(Kategori, id=kategori_id)
        kategori.delete()
        messages.success(request, 'Kategori berhasil dihapus')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

##########################################################################################

# CREATE Penulis
def penulis_create(request):
    if request.method == 'POST':
        form = PenulisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Penulis berhasil ditambahkan!')
            return redirect('penulis_index')
        else:
            print(form.errors)
    else:
        form = PenulisForm()
    return render(request, 'penulis/create.html', {'form': form})

# READ Penulis (Index)
def penulis_index(request):
    query = request.GET.get('q')
    penulis_list = Penulis.objects.all()
    if query:
        penulis_list = Penulis.objects.filter(
            Q(nama_penulis__icontains=query) |
            Q(biodata__icontains=query)
        ).distinct()
    return render(request, 'penulis/index.html', {'penulis_list': penulis_list, 'query': query})

# UPDATE Penulis
def penulis_update(request, penulis_id):
    penulis = get_object_or_404(Penulis, id_penulis=penulis_id)
    if request.method == 'POST':
        form = PenulisForm(request.POST, request.FILES, instance=penulis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data penulis berhasil diubah!')
            return redirect('penulis_index')
        else:
            messages.error(request, 'Terjadi kesalahan saat mengubah data penulis.')
    else:
        form = PenulisForm(instance=penulis)
    return render(request, 'penulis/update.html', {'form': form, 'penulis': penulis})

# DELETE Penulis
def penulis_delete(request, id_penulis):
    if request.method == 'POST':
        penulis = get_object_or_404(Penulis, id_penulis=id_penulis)
        penulis.delete()
        messages.success(request, 'Penulis berhasil dihapus')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

def detail_buku(request): 
    return render(request, 'page/detail_buku.html')

def daftar_buku(request): 
    return render(request, 'page/daftar_buku.html')

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

