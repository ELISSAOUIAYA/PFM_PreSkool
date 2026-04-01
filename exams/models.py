from django.db import models

class Subject(models.Model):
    """Représente une matière (ex: Python, Mathématiques)"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de la matière")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code Matière")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"


class Exam(models.Model):
    """Représente un examen spécifique lié à une matière"""
    EXAM_TYPES = [
        ('CC', 'Contrôle Continu'),
        ('EF', 'Examen Final'),
        ('DS', 'Devoir Surveillé'),
    ]

    name = models.CharField(max_length=150, verbose_name="Nom de l'examen")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exams", verbose_name="Matière")
    date = models.DateField(verbose_name="Date de l'examen")
    exam_type = models.CharField(max_length=2, choices=EXAM_TYPES, default='CC', verbose_name="Type d'examen")
    total_marks = models.PositiveIntegerField(default=20, verbose_name="Note Maximale")

    def __str__(self):
        return f"{self.name} - {self.subject.name}"

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examens"