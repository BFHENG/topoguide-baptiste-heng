from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from .models import Itineraire, Sortie
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import SortieForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def liste_itineraires(request):
    
    liste_itineraires = get_list_or_404(Itineraire)
    
    return render(request, 'itineraires/liste_itineraires.html', {'liste_itineraires': liste_itineraires})

def details_itineraire(request, itineraire_id):
    
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    
    return render(request, 'itineraires/details_itineraire.html', {'itineraire': itineraire})
    
def details_sortie(request, itineraire_id, sortie_id):
    
    sortie = get_object_or_404(Sortie, pk = sortie_id)
    
    return render(request, 'itineraires/details_sortie.html', {'sortie': sortie})

@login_required()
def nouvelle_sortie(request):
    
    if request.method == 'GET':
        form = SortieForm()
        
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_itineraires')
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})



@login_required()    
def modif_sortie(request, sortie_id):
    
    sortie = Sortie.objects.get(pk=sortie_id)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            return redirect('liste_itineraires')
    return render(request, 'itineraires/modif_sortie.html', {'form': form})


def login_view(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

