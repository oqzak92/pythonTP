from django import forms
from django.contrib import admin
from .models import Voiture

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'couleur', 'prix'] 





class VoitureAdmin(admin.ModelAdmin):
    form = VoitureForm
    list_display = ('marque', 'modele', 'couleur', 'prix')
    search_fields = ('marque', 'modele')
    list_filter = ('couleur',)
    ordering = ('prix',)

admin.site.register(Voiture, VoitureAdmin)