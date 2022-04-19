from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Itineraire, Sortie
from django.http import HttpResponse
from django.template import loader

def liste_itineraires(request):
    
    liste_itineraires = get_list_or_404(Itineraire)
    #template = loader.get_template('itineraires/liste_itineraires.html')
    #context = {
    #    'liste_itineraires': liste_itineraires,
    #}
    
    #return HttpResponse(template.render(context, request))
    return render(request, 'itineraires/liste_itineraires.html', {'liste_itineraires': liste_itineraires})

def details_itineraire(request, itineraire_id):
    
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    
    return render(request, 'itineraires/details_itineraire.html', {'itineraire': itineraire})
    
def details_sortie(request, itineraire_id, sortie_id):
    
    sortie = get_object_or_404(Sortie, pk = sortie_id)
    
    return render(request, 'itineraires/details_sortie.html', {'sortie': sortie})

