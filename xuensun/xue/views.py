from django.shortcuts import render



def detail_buku(request): 
    return render(request, 'page/detail_buku.html')

def daftar_buku(request): 
    return render(request, 'page/daftar_buku.html')

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

