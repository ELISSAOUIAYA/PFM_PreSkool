from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # Ce que l'on voit dans la liste
    list_display = ('name', 'code', 'head_teacher', 'created_at')
    
    # Les filtres sur le côté droit
    list_filter = ('created_at',) 
    
    # La barre de recherche
    search_fields = ('name', 'code')
    
    # L'ordre par défaut (alphabétique sur le nom)
    ordering = ('name',)
    
    # Organisation du formulaire d'édition
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'code')
        }),
        ('Détails', {
            'fields': ('description', 'head_teacher')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',) # Masqué par défaut
        }),
    )
    
    # Empêcher la modification manuelle des dates de création
    readonly_fields = ('created_at','updated_at')