from django.db import models
from subjects.models import Subject
from student.models import Student

class Exam(models.Model):
    EXAM_TYPES = [
        ('Quiz', 'Quiz'),
        ('Midterm', 'Examen Mi-parcours'),
        ('Final', 'Examen Final'),
    ]

    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPES)
    total_marks = models.IntegerField(default=100) 

    def __str__(self):
        return f"{self.name} - {self.subject.name}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='marks')
    score = models.FloatField()

    def __str__(self):
        return f"{self.student} | {self.exam.name} : {self.score}"