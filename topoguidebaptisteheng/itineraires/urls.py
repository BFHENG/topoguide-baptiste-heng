from django.urls import path

from . import views

urlpatterns = [
    path('', views.liste_itineraires, name='liste_itineraires'),
    
    path('<int:itineraire_id>/', views.details_itineraire, name = 'details_itineraire')
]