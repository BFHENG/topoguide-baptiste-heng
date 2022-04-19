from django.db import models

class Itineraire(models.Model):
    """ 
    Un itinéraire
    """
    titre = models.CharField(max_length=200)
    point_de_depart = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    alt_depart = models.FloatField('Altitude (m)') 
    alt_min = models.FloatField('Altitude minimale (m)') 
    alt_max = models.FloatField('Altitude maximale (m)') 
    deniv_pos_cumul = models.FloatField('Denivele positif cumule (m)') 
    deniv_neg_cumul = models.FloatField('Denivele negatif cumule (m)') 
    
    duree = models.IntegerField('Durée (h)')
    
    class NiveauxDifficulte(models.IntegerChoices):
        IMPOSSIBLE = 5
        EPUISANT = 4
        NORMAL = 3
        PROMENADE = 2
        REPOS = 1
        

    difficulte = models.IntegerField(choices=NiveauxDifficulte.choices)
    
    def __str__(self):
        return self.titre
    
class Sortie(models.Model):
    """
    Une sortie
    """
    nom_utilisateur = models.CharField(max_length=200)
    itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
    date_sortie = models.DateTimeField('date sortie')

    duree = models.IntegerField('Durée (h)')
    nombre_personnes = models.IntegerField('Nombre de personnes')
    
    class NiveauxExperience(models.IntegerChoices):
        DEBUTANTS = 1
        MIXTE = 2
        EXPERIMENTES = 3
        
    
    experience = models.IntegerField(choices=NiveauxExperience.choices)
    
    class Meteos(models.IntegerChoices):
        MAUVAISE = 1
        MOYENNE = 2
        BONNE = 3
    
    meteo = models.IntegerField(choices=Meteos.choices)
    
    class NiveauxDifficulte(models.IntegerChoices):
        IMPOSSIBLE = 5
        EPUISANT = 4
        NORMAL = 3
        PROMENADE = 2
        REPOS = 1
        
    difficulte =models.IntegerField(choices=NiveauxDifficulte.choices)
    
    def __str__(self):
        return self.itineraire
    
    
    
# Create your models here.
