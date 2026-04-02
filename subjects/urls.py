from django.urls import path
from . import views

urlpatterns = [
    # Liste des matières
    path('subjects/', views.subject_list, name='subject-list'),
    
    # Détails d'une matière
    path('subjects/<int:pk>/', views.subject_detail, name='subject-detail'),
    
    # Créer une nouvelle matière
    path('subjects/create/', views.subject_create, name='subject-create'),
    
    # Modifier une matière
    path('subjects/<int:pk>/edit/', views.subject_update, name='subject-update'),
    
    # Supprimer une matière
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject-delete'),
]
