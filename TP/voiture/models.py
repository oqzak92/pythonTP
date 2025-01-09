from django.db import models

# Create your models here.

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)


    
