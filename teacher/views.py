from django.shortcuts import render
from .models import Teacher
from django.shortcuts import redirect
from home_auth.models import CustomUser
from departments.models import Department
from .models import Teacher
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        # 1. Création de l'utilisateur
        user = CustomUser.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            is_teacher=True # Très important pour tes rôles !
        )
        
        # 2. Création du profil Teacher lié
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

def teacher_dashboard(request):
    count = Teacher.objects.count()
    context = {
        'total_teachers': count,
    }
    return render(request, 'teacher/teacher_dashboard.html', context)
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    user = teacher.user # On récupère l'utilisateur lié
    
    if request.method == "POST":
        # 1. Mise à jour de la table USER (Nom, Prénom, Email)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save() # On enregistre l'utilisateur

        # 2. Mise à jour de la table TEACHER (Téléphone, Département, Genre)
        teacher.phone = request.POST.get('phone')
        teacher.gender = request.POST.get('gender')
        
        # Pour le département, on récupère l'objet
        dept_id = request.POST.get('department')
        teacher.department = get_object_or_404(Department, id=dept_id)
        
        teacher.save() # On enregistre le professeur
        
        return redirect('teacher_list')

    departments = Department.objects.all()
    return render(request, 'teacher/edit_teacher.html', {
        'teacher': teacher,
        'departments': departments
    })
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    nom_prof = f"{teacher.user.first_name} {teacher.user.last_name}"
    teacher.delete()
    messages.success(request, f"L'enseignant {nom_prof} a été supprimé avec succès.")
    
    return redirect('teacher_list')
