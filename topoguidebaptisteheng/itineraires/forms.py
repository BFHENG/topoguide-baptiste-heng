from django import forms
from .models import Sortie

class SortieForm(forms.ModelForm):
    """
    Formulaire de sortie, prenant en entrée les informations précisées dans sortie.models.py
    """
    class Meta :
        model = Sortie
        fields = '__all__' 