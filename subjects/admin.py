from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code','teacher', 'department', 'credit_hours', 'is_optional', 'created_at')
    list_filter = ('department', 'is_optional', 'created_at')
    search_fields = ('name', 'code')
    ordering = ('department', 'name')
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'code','teacher', 'department')
        }),
        ('Détails Académiques', {
            'fields': ('description', 'credit_hours', 'is_optional')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
