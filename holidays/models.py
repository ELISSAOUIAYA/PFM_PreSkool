from django.db import models

class Holiday(models.Model):
    """Gestion des jours fériés et vacances"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_national_holiday = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Jour férié"
        verbose_name_plural = "Jours fériés"
        ordering = ['start_date']

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"
