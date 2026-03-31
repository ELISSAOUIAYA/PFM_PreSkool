from django.contrib import admin
from .models import Holiday

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_national_holiday', 'created_at')
    list_filter = ('is_national_holiday', 'created_at')
    search_fields = ('name',)
    ordering = ('-start_date',)
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'description')
        }),
        ('Période', {
            'fields': ('start_date', 'end_date')
        }),
        ('Classification', {
            'fields': ('is_national_holiday',)
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
