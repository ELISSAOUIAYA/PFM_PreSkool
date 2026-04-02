from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Mark
from holidays.models import Holiday
from subjects.models import Subject
from student.models import Student, Parent
from django.contrib import messages

# 1. Liste des étudiants (LA SEULE VERSION)
def student_list(request):
    students = Student.objects.all()
    count_students = students.count()
    
    context = {
        'student_list': students, # Le nom doit correspondre au {% for student in student_list %} du HTML
        'count_students': count_students,
    }
    # Assure-toi que le chemin correspond au nom du dossier qu'on a renommé (student sans 's')
    return render(request, 'student/student_list.html', context)

# 2. Le Dashboard Étudiant
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
    return render(request, 'student/student-dashboard.html', context)

# 3. Ajouter un étudiant (Utilise ta version complète avec POST)
def add_student(request):
    if request.method == 'POST':
        # ... (garde tout ton code de récupération de données ici) ...
        # Après la création du parent et de l'étudiant :
        messages.success(request, 'Student added Successfully')
        return redirect('student_list')
    
    return render(request, 'student/add_student.html')

# 4. Voir un étudiant spécifique
def view_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student/student-details.html', {'student': student})

# 5. Modifier un étudiant
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student/edit_student.html', {'student': student})

# 6. Supprimer un étudiant
def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student.delete()
    messages.info(request, 'Student deleted.')
    return redirect('student_list')