from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Subject
from django.contrib import messages

# 1. Voir la liste
def exam_list_view(request):
    exams = Exam.objects.all().select_related('subject')
    return render(request, 'exams/exam_list.html', {'exams': exams})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, Subject
from django.contrib import messages

# 2. Ajouter un examen
def add_exam_view(request):
    if request.method == "POST":
        # Ces variables doivent être définies AVANT le bloc try
        name = request.POST.get('name')
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        exam_type = request.POST.get('exam_type')
        
        try:
            subject = Subject.objects.get(id=subject_id)
            Exam.objects.create(
                name=name,
                subject=subject,
                date=date,
                exam_type=exam_type
            )
            messages.success(request, "Examen ajouté !")
            return redirect('exam_list') # L'indentation ici est cruciale
            
        except (Subject.DoesNotExist, ValueError):
            messages.error(request, "Erreur : La matière sélectionnée est invalide")

    # Cette partie s'exécute si c'est un GET ou s'il y a une erreur
    subjects = Subject.objects.all()
    return render(request, 'exams/add_exam_form.html', {'subjects': subjects})

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