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
    
class Sortie(models.Model):
    """
    Une sortie
    """
    nom_utilisateur = models.CharField(max_length=200)
    itineraire = models.ForeignKey('Album', on_delete=models.CASCADE)
    date_sortie = models.DateTimeField('date sortie')

    duree = models.IntegerField('Durée (h)')
    nombre_personnes = models.IntegerField('Nombre de personnes')
    
    EXPERIENCES = [
        ('td', 'Tous débutants')
        ('te', 'Tous experimentés')
        ('mi', 'Mixte')
    ]
    
    experience = models.CharField(
        max_length=2,
        choices=EXPERIENCES,
        default= 'td',
    )
    
    METEOS = [
        ('bo', 'Bonne')
        ('mo', 'Moyenne')
        ('ma', 'Mauvaise')
    ]
    
    meteo = experience = models.CharField(
        max_length=2,
        choices=METEOS,
        default= 'mo',
    )
    
    
    class NiveauxDifficulte(models.IntegerChoices):
        IMPOSSIBLE = 5
        EPUISANT = 4
        NORMAL = 3
        PROMENADE = 2
        REPOS = 1
        
    difficulte =models.IntegerField(choices=NiveauxDifficulte.choices)
    
    
    
# Create your models here.
