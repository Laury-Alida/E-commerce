
from django.shortcuts import render, get_object_or_404

from store.models import Produit


# Create your views here.
def index(request):
    produits = Produit.objects.all()
    return render(request, 'store/index.html', context={'produits': produits})

def detail_produit(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    return render(request, 'store/detail.html', context={'produit': produit})