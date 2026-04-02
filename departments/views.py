from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Department
from teacher.models import Teacher
from django.contrib.auth.models import User

@login_required
def department_list(request):
    """Affiche la liste de tous les départements"""
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'departments/department_list.html', context)

@login_required
def department_detail(request, pk):
    """Affiche les détails d'un département avec ses filières et professeurs"""
    department = get_object_or_404(Department, pk=pk)
    context = {'department': department}
    return render(request, 'departments/department_detail.html', context)

@login_required
def department_create(request):
    """Crée un nouveau département"""
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        description = request.POST.get('description', '')
        head_teacher = request.POST.get('head_teacher', '')
        
        department = Department.objects.create(
            name=name,
            code=code,
            description=description,
            head_teacher=head_teacher
        )
        return redirect('department-detail', pk=department.pk)
    
    return render(request, 'departments/department_form.html')

@login_required
def department_update(request, pk):
    """Modifie un département existant"""
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.code = request.POST.get('code')
        department.description = request.POST.get('description')
        department.head_teacher = request.POST.get('head_teacher')
        department.save()
        return redirect('department-detail', pk=department.pk)
    
    context = {'department': department}
    return render(request, 'departments/department_form.html', context)

@login_required
def department_delete(request, pk):
    """Supprime un département"""
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        department.delete()
        return redirect('department-list')
    
    context = {'department': department}
    return render(request, 'departments/department_confirm_delete.html', context)

@login_required
def add_teacher_to_department(request, pk):
    """Ajoute un professeur à un département"""
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        teacher = get_object_or_404(Teacher, pk=teacher_id)
        teacher.department = department
        teacher.save()
        return redirect('department-detail', pk=department.pk)
    
    # Afficher seulement les professeurs qui ne sont pas encore assignés à un département
    # ou ceux assignés à d'autres départements
    available_teachers = Teacher.objects.exclude(department=department)
    context = {
        'department': department,
        'available_teachers': available_teachers
    }
    return render(request, 'departments/add_teacher_to_department.html', context)
