from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Mark
from holidays.models import Holiday
from subjects.models import Subject
# Importe ton modèle Student ici si tu en as un, par exemple :
# from .models import Student 

# 1. Le Dashboard Étudiant
@login_required
def student_dashboard(request):
    username = request.user.username
    context = {
        'timetables': [], 
        'upcoming_exams': Exam.objects.order_by('date')[:3],
        'latest_results': Mark.objects.filter(student__first_name=username).order_by('-id')[:5],
        'holidays': Holiday.objects.all().order_by('start_date')[:3],
        'my_subjects': Subject.objects.all(),
    }
    return render(request, 'students/student-dashboard.html', context)

# 2. Voir un étudiant spécifique (C'est celle qui manquait !)
def view_student(request, student_id):
    # Pour l'instant, on renvoie juste vers le template
    return render(request, 'student/view_student.html', {'id': student_id})

# 3. Ajouter un étudiant
def add_student(request):
    return render(request, 'student/add_student.html')

# 4. Liste des étudiants
def student_list(request):
    return render(request, 'student/student_list.html')

# 5. Modifier un étudiant
def edit_student(request, pk):
    return render(request, 'student/edit_student.html')

# 6. Supprimer un étudiant
def delete_student(request, pk):
    return redirect('student_list')