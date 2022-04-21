from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Itineraire, Sortie
from django.http import HttpResponse
from django.template import loader
from .forms import SortieForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def liste_itineraires(request):
    """Liste des itinéraires

    Args:
        request (GET) : Récupère la liste des itinéraires de la base de données

    Returns:
        - une page listant ces itinéraires
    """ 
    liste_itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/liste_itineraires.html', {'liste_itineraires': liste_itineraires})

def details_itineraire(request, itineraire_id):
    """Liste des sorties associées à un itinéraire

    Args:
        request (GET): Récupère l'itinéraire sur lequel on a cliqué sur la page d'accueil
        itineraire_id (database ID): ID associé à l'itinéraire dont on veut voir les sorties associées

    Returns:
        - une page listant les sorties associées à un itinéraire
    """
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request, 'itineraires/details_itineraire.html', {'itineraire': itineraire})
    
def details_sortie(request, itineraire_id, sortie_id):
    """Détails d'une sortie

    Args:
        request (GET): Récupère une sortie précise d'un sportif
        itineraire_id (database ID): ID associé à l'itinéraire
        sortie_id (database ID): ID associé à la sortie dont on veut voir les détails

    Returns:
        - une page listant les informations de l'itinéraire puis les détails du sportif sur sa propre sortie
    """
    
    sortie = get_object_or_404(Sortie, pk = sortie_id)
    
    
    return render(request, 'itineraires/details_sortie.html', {'sortie': sortie})


def nouvelle_sortie(request):
    """Bouton de nouvelle sortie, disponible seulement si l'utilisateur est connecté

    Args:
        request (GET ou POST): Récupère le form à remplir pour créer une nouvelle sortie, et le renvoie à la base de données

    Returns:
        - formulaire à remplir pour ajouter une sortie
    """
    if request.method == 'GET':
        form = SortieForm()
        
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_itineraires')
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})


def modif_sortie(request, sortie_id):
    """Bouton de modification de sortie, disponible seulement si l'utilisateur connecté est celui ayant effectué la sortie

    Args:
        request (GET ou POST): Récupère le form à remplir pour modifier la sortie, et le renvoie à la base de données
        sortie_id (ID database): On récupère les informations de la sortie à modifier

    Returns:
        - formulaire pré-remplit à modifier pour changer les informations d'une sortie
    """
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
    """Connexion au site

    Args:
        request (POST): Récupère le form à remplir pour se connecter

    Returns:
        - une formulaire d'authentification à remplir pour se connecter
    """
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """Déconnexion du site

    Args:
        request (POST) : se déconnecte du site

    Returns:
        - retour à la page d'accueil, l'utilisateur n'est plus connecté
    """
    logout(request)
    return liste_itineraires(request)

