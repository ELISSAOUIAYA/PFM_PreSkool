from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Subject
from departments.models import Department


# ==================== VUES BASÉES SUR DES FONCTIONS ====================

@login_required
def subject_list(request):
    """Affiche la liste de toutes les matières"""
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects/subject_list.html', context)


@login_required
def subject_detail(request, pk):
    """Affiche les détails d'une matière"""
    subject = get_object_or_404(Subject, pk=pk)
    context = {'subject': subject}
    return render(request, 'subjects/subject_detail.html', context)


@login_required
def subject_create(request):
    """Crée une nouvelle matière"""
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        department_id = request.POST.get('department')
        description = request.POST.get('description', '')
        credit_hours = request.POST.get('credit_hours', 3)
        is_optional = request.POST.get('is_optional') == 'on'
        
        subject = Subject.objects.create(
            name=name,
            code=code,
            department_id=department_id,
            description=description,
            credit_hours=credit_hours,
            is_optional=is_optional
        )
        return redirect('subject-detail', pk=subject.pk)
    
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'subjects/subject_form.html', context)


@login_required
def subject_update(request, pk):
    """Modifie une matière existante"""
    subject = get_object_or_404(Subject, pk=pk)
    
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        subject.department_id = request.POST.get('department')
        subject.description = request.POST.get('description')
        subject.credit_hours = request.POST.get('credit_hours')
        subject.is_optional = request.POST.get('is_optional') == 'on'
        subject.save()
        return redirect('subject-detail', pk=subject.pk)
    
    departments = Department.objects.all()
    context = {'subject': subject, 'departments': departments}
    return render(request, 'subjects/subject_form.html', context)


@login_required
def subject_delete(request, pk):
    """Supprime une matière"""
    subject = get_object_or_404(Subject, pk=pk)
    
    if request.method == 'POST':
        subject.delete()
        return redirect('subject-list')
    
    context = {'subject': subject}
    return render(request, 'subjects/subject_confirm_delete.html', context)
