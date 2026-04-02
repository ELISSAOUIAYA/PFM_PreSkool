from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du Département")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    head_teacher = models.CharField(max_length=100, blank=True, null=True, verbose_name="Chef de Département")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"