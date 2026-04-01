from django.urls import path
from . import views

urlpatterns = [
    # Liste des départements
    path('departments/', views.department_list, name='department-list'),
    
    # Détails d'un département
    path('departments/<int:pk>/', views.department_detail, name='department-detail'),
    
    # Créer un nouveau département
    path('departments/create/', views.department_create, name='department-create'),
    
    # Modifier un département
    path('departments/<int:pk>/edit/', views.department_update, name='department-update'),
    
    # Supprimer un département
    path('departments/<int:pk>/delete/', views.department_delete, name='department-delete'),
    
    # Ajouter un professeur à un département
    path('departments/<int:pk>/add-teacher/', views.add_teacher_to_department, name='add-teacher-to-department'),
]
