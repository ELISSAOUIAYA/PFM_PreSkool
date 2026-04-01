from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Subject
from django.contrib import messages

# 1. Voir la liste
def exam_list_view(request):
    exams = Exam.objects.all().select_related('subject')
    return render(request, 'exams/exam_list.html', {'exams': exams})

# 2. Ajouter un examen
def add_exam_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        exam_type = request.POST.get('exam_type')
        
        subject = Subject.objects.get(id=subject_id)
        Exam.objects.create(name=name, subject=subject, date=date, exam_type=exam_type)
        messages.success(request, "Examen ajouté !")
        return redirect('exam_list')
    
    subjects = Subject.objects.all()
    return render(request, 'exams/add_results.html', {'subjects': subjects}) # Utilise ton fichier existant

# 3. Supprimer un examen
def delete_exam_view(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    messages.warning(request, "Examen supprimé.")
    return redirect('exam_list')

# 4. Voir les résultats
def results_list_view(request):
    exams = Exam.objects.all()
    return render(request, 'exams/my_results.html', {'results': exams})