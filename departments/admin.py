from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_of_department', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'code')
    ordering = ('name',)
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'code')
        }),
        ('Détails', {
            'fields': ('description', 'head_of_department')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
