from django.shortcuts import render
from .models import Teacher
from django.shortcuts import redirect
from home_auth.models import CustomUser
from departments.models import Department
from .models import Teacher

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