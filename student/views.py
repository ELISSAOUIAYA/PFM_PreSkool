from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return HttpResponse("Page de liste des étudiants (Bientôt disponible)")

def add_student(request):
    return HttpResponse("Page d'ajout d'étudiant (Bientôt disponible)")
