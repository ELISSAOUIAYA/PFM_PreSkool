from django.db import models

class Department(models.Model):
<<<<<<< HEAD
    """Gestion des départements de l'établissement"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    head_of_department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ['name']

    def __str__(self):
        return self.name
=======
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    # On met null=True car au début le département n'a peut-être pas encore de responsable
    head_teacher = models.OneToOneField(
        'teacher.Teacher', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='headed_department'
    )

    def __str__(self):
        return self.name
>>>>>>> 4080006f24c039c4831eaec79e80e170c62651d0
