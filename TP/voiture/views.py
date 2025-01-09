from django.shortcuts import render, redirect, get_object_or_404
from .models import Voiture
from .forms import VoitureForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# def Show_voiture(request):
#     voiture = Voiture.objects.all()
#     return render(request, 'voiture/liste_voitures.html', {'voiture': voiture})


def Show_voiture(request):
    marques = Voiture.objects.values_list('marque', flat=True).distinct()
    marque_filtre = request.GET.get('marque')  
    if marque_filtre:
        voiture = Voiture.objects.filter(marque=marque_filtre)
    else:
        voiture = Voiture.objects.all()
        

    return render(request, 'voiture/liste_voitures.html', {
        'voitures': voiture,
        'marques': marques,     
        'tout': "Tous"           
    })




def detail_voiture(request, id_voiture):
    voiture = get_object_or_404(Voiture, id=id_voiture)


    # partie pour la suppresion
    if request.method == 'POST':
        voiture.delete()  
        return redirect('voiture:home')  
    



    return render(request, 'voiture/voiture_detail.html', {'voiture': voiture})




@login_required
def Add_voiture(request):
    if request.method == 'POST':
        addvoiture = VoitureForm(request.POST)
        if addvoiture.is_valid(): 
            addvoiture.save()  
            return redirect('voiture:home')  
    else:
        addvoiture = VoitureForm()  

    return render(request, 'voiture/ajouter_voiture.html', {'addvoiture': addvoiture})  





