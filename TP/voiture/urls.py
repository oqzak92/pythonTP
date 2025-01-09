from django.urls import path
from . import views

app_name = 'voiture'  # N'oubliez pas de définir un nom pour l'application

urlpatterns = [
    path('', views.Show_voiture, name='home'),  # page d'accueil
    path('ajouter/', views.Add_voiture, name='ajouter_voiture'),  # page pour ajouter une voiture
    path('detail/<int:id_voiture>/', views.detail_voiture, name='detail_voiture'), # page pour voir les detail d'une voiture

]
