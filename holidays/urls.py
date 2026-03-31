from django.urls import path
from . import views

urlpatterns = [
    # Liste des jours fériés
    path('holidays/', views.holiday_list, name='holiday-list'),
    
    # Détails d'un jour férié
    path('holidays/<int:pk>/', views.holiday_detail, name='holiday-detail'),
    
    # Créer un nouveau jour férié
    path('holidays/create/', views.holiday_create, name='holiday-create'),
    
    # Modifier un jour férié
    path('holidays/<int:pk>/edit/', views.holiday_update, name='holiday-update'),
    
    # Supprimer un jour férié
    path('holidays/<int:pk>/delete/', views.holiday_delete, name='holiday-delete'),
]
