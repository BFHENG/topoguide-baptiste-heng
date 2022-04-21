from django.contrib import admin
from .models import Itineraire, Sortie

# Permet à l'administrateur de rentrer des itinéraires et des sorties

admin.site.register(Itineraire)
admin.site.register(Sortie)
