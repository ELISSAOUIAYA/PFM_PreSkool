from django.db import models

class Department(models.Model):
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