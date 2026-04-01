from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

# On importe tous les modèles nécessaires ici une seule fois
from .models import Mark, Exam
from subjects.models import Subject
from student.models import Student

# 1. Voir la liste des examens
def exam_list_view(request):
    exams = Exam.objects.all().select_related('subject')
    return render(request, 'exams/exam_list.html', {'exams': exams})

# 2. Ajouter un examen
@staff_member_required
def add_exam_view(request):
    if request.method == "POST":
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
            return redirect('exam_list')
        except (Subject.DoesNotExist, ValueError):
            messages.error(request, "Erreur : La matière sélectionnée est invalide")

    subjects_list = Subject.objects.all()
    return render(request, 'exams/add_exam_form.html', {'subjects': subjects_list})

# 3. Supprimer un examen
@staff_member_required
def delete_exam_view(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    messages.warning(request, "Examen supprimé.")
    return redirect('exam_list')

# 4. Saisir les notes (Section ajout)
@staff_member_required
def add_mark_view(request):
    if request.method == "POST":
        s_id = request.POST.get('student_id')
        e_id = request.POST.get('exam_id')
        score = request.POST.get('score')
        
        Mark.objects.create(
            student_id=s_id,
            exam_id=e_id,
            score=score
        )
        messages.success(request, "Note enregistrée avec succès !")
        return redirect('exam_list')

    context = {
        'students': Student.objects.all(),
        'exams': Exam.objects.all(),
    }
    return render(request, 'exams/add_results.html', context)

# 5. Afficher les notes (Section affichage)
def results_list_view(request):
    # Si c'est un prof/admin, il voit tout. Sinon, l'élève voit ses notes.
    if request.user.is_staff:
        results = Mark.objects.all().select_related('student', 'exam')
    else:
        results = Mark.objects.filter(student__first_name=request.user.username).select_related('exam')
        
    return render(request, 'exams/my_results.html', {'results': results})