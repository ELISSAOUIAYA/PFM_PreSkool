from django.contrib import admin
from .models import Subject, Exam

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')  # Affiche le nom et le code dans la liste
    search_fields = ('name', 'code') # Permet de chercher par nom ou code

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date', 'exam_type', 'total_marks') # Colonnes visibles
    list_filter = ('subject', 'exam_type', 'date') # Filtres sur le côté droit
    search_fields = ('name',) # Barre de recherche
    date_hierarchy = 'date'   # Navigation rapide par date en haut de la liste