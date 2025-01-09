from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        insc = UserCreationForm(request.POST)
        if insc.is_valid():
            insc.save()
            return redirect('voiture:home')  # Redirige vers la page de login
    else:
        insc = UserCreationForm()
    return render(request, 'comptes/register.html', {'insc': insc})



def logout_view(request):
    logout(request)
    return redirect('voiture:home') 


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            conect = True  
            return redirect('voiture:home')  
        else:
            conect = False  
    else:
        form = AuthenticationForm()  
        conect = None  

    return render(request, 'comptes/login.html', {'form': form, 'conect': conect})