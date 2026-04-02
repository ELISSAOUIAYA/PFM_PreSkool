from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import CustomUser 
from student.models import Student

def signup_view(request): 
    if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        role = request.POST.get('role')  # student, teacher ou admin 
 
        # Créer l'utilisateur 
        user = CustomUser.objects.create_user( 
            username=email, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
        ) 
 
        # Assigner le rôle
        if role == 'student': 
            user.is_student = True 
        elif role == 'teacher': 
            user.is_teacher = True 
        elif role == 'admin': 
            user.is_admin = True 
 
        user.save() 
        login(request, user) 
        messages.success(request, 'Signup successful!') 
        return redirect('login') 
    return render(request, 'authentication/register.html')

def login_view(request): 
    if request.method == 'POST': 
        email = request.POST['email'] 
        password = request.POST['password'] 
 
        user = authenticate(request, username=email, 
                            password=password) 
        if user is not None: 
            login(request, user) 
            messages.success(request, 'Login successful!') 
            # Redirection selon le rôle 
            if user.is_admin or user.is_superuser:
                return redirect('admin_dashboard') 
            elif user.is_teacher: 
                return redirect('teacher_dashboard') 
            elif user.is_student:
                return redirect('dashboard') 
            else: 
                messages.error(request, 'Invalid user role') 
                return redirect('login') 
        else: 
            messages.error(request, 'Invalid credentials') 
    return render(request, 'authentication/login.html') 

def logout_view(request): 
    logout(request) 
    messages.success(request, 'You have been logged out.') 
    return redirect('login') 

def forgot_password_view(request):
    return render(request, 'authentication/forgot-password.html') 

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('login')
    
    total_students = Student.objects.count()
    return render(request, 'index.html', {'total_students': total_students})

@login_required
def user_list(request):
    if not request.user.is_admin:
        return redirect('login')
    
    # On récupère tous les utilisateurs
    all_users = CustomUser.objects.all().order_by('-id')
    return render(request, 'authentication/user_list.html', {'users': all_users})

def delete_user(request, user_id):
    user_to_delete = CustomUser.objects.get(id=user_id)
    # Empêcher l'admin de se supprimer lui-même par erreur !
    if user_to_delete != request.user:
        user_to_delete.delete()
        messages.success(request, "Utilisateur supprimé !")
    return redirect('user_list')
