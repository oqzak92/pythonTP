from django import forms
from .models import Voiture


class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'couleur', 'prix']
