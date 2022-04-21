from django.urls import path

from . import views

urlpatterns = [
    # ex: /itineraires/
    path('', views.liste_itineraires, name='liste_itineraires'),
    
    # ex: /itineraires/1/
    path('<int:itineraire_id>/', views.details_itineraire, name = 'details_itineraire'),
    
    # ex: /itineraires/1/2/
    path('<int:itineraire_id>/<int:sortie_id>/', views.details_sortie, name = 'details_sortie'),
    
    # ex: /itineraires/nouvelle_sortie/
    path('nouvelle_sortie/', views.nouvelle_sortie, name = 'nouvelle_sortie'),
    
    # ex: /itineraires/modif_sortie/13/
    path('modif_sortie/<int:sortie_id>/', views.modif_sortie, name = 'modif_sortie'),
    
    # ex: /itineraires/accounts/login/
    path('accounts/login/', views.login_view, name = 'login_view'),
    
    # ex: /itineraires/accounts/logout
    path('accounts/logout/', views.logout_view, name = 'logout_view')
]