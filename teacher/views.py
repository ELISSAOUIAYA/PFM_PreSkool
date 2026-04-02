from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # <--- NE PAS OUBLIER CELUI-LA
from django.contrib import messages
from .models import Teacher
from home_auth.models import CustomUser
from departments.models import Department
from student.models import Student
from subjects.models import Subject

# 1. Liste des professeurs
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

# 2. Ajouter un professeur
def add_teacher(request):
    if request.method == 'POST':
        user = CustomUser.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            is_teacher=True
        )
        
        dept = Department.objects.get(id=request.POST['department'])
        Teacher.objects.create(
            user=user,
            employee_id=request.POST['employee_id'],
            department=dept,
            gender=request.POST['gender'],
            phone=request.POST['phone']
        )
        return redirect('teacher_list')
    
    departments = Department.objects.all()
    return render(request, 'teacher/add_teacher.html', {'departments': departments})

# 3. LE DASHBOARD (Version unique et complète)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def teacher_dashboard(request):
    # --- DONNÉES FICTIVES POUR LA VIDÉO ---
    
    # On crée un faux objet 'teacher' (sans toucher à la base de données)
    class MockTeacher:
        def __init__(self):
            self.id = 1
            self.employee_id = "T2026-FSTT"
            self.phone = "+212 6 99 00 11 22"
            self.gender = "Femme"
            self.photo = None  # Tu peux laisser None pour l'icône par défaut
            self.department = type('obj', (object,), {'name': 'Génie Informatique (IDAI)'})

    # On crée une liste de fausses matières
    my_subjects = [
        {'name': 'Développement Web (Django)', 'code': 'WEB202', 'credit_hours': 4},
        {'name': 'Bases de Données Avancées', 'code': 'DB301', 'credit_hours': 3},
        {'name': 'Algorithmique & C++', 'code': 'ALG101', 'credit_hours': 5},
    ]

    context = {
        'teacher': MockTeacher(), # On envoie le faux prof
        'my_subjects': my_subjects, # On envoie les fausses matières
    }
    
    return render(request, 'teacher/teacher_dashboard.html', context)

# 4. Modifier un professeur
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    user = teacher.user
    
    if request.method == "POST":
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        teacher.phone = request.POST.get('phone')
        teacher.gender = request.POST.get('gender')
        dept_id = request.POST.get('department')
        teacher.department = get_object_or_404(Department, id=dept_id)
        teacher.save()
        
        return redirect('teacher_list')

    departments = Department.objects.all()
    return render(request, 'teacher/edit_teacher.html', {
        'teacher': teacher,
        'departments': departments
    })

# 5. Supprimer un professeur
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    nom_prof = f"{teacher.user.first_name} {teacher.user.last_name}"
    
    # On supprime l'utilisateur (le profil Teacher partira avec grâce au CASCADE)
    user = teacher.user
    user.delete()
    
    messages.success(request, f"L'enseignant {nom_prof} a été supprimé avec succès.")
    return redirect('teacher_list')