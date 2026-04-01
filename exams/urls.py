from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.exam_list_view, name='exam_list'),
    path('ajouter/', views.add_exam_view, name='add_exam'),
    path('supprimer/<int:pk>/', views.delete_exam_view, name='delete_exam'),
    path('resultats/', views.results_list_view, name='results_list'),
    path('marks/add/', views.add_mark_view, name='add_mark'),
    path('results/', views.results_list_view, name='my_results'),
]