from django.db import models
from departments.models import Department

class Subject(models.Model):
    """Gestion des matières / cours"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    credit_hours = models.IntegerField(default=3)
    is_optional = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"
        ordering = ['name']
        unique_together = ('name', 'department')

    def __str__(self):
        return f"{self.name} ({self.department.code})"
