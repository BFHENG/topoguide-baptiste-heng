from django.urls import path

from . import views

urlpatterns = [
    path('', views.liste_itineraires, name='liste_itineraires'),
    
    path('<int:itineraire_id>/', views.details_itineraire, name = 'details_itineraire'),
    
    path('<int:itineraire_id>/<int:sortie_id>/', views.details_sortie, name = 'details_sortie'),
    
    path('nouvelle_sortie/', views.nouvelle_sortie, name = 'nouvelle_sortie'),
    
    path('modif_sortie/<int:sortie_id>/', views.modif_sortie, name = 'modif_sortie'),
    
    path('accounts/login/', views.login_view, name = 'login_view'),
    
    path('accounts/logout/', views.logout_view, name = 'logout_view')
]