from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Mark, Exam
from subjects.models import Subject
from student.models import Student

# --- SECTION EXAMENS ---
@login_required
def exam_list_view(request):
    exams = Exam.objects.all().order_by('date')
   
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
            # CORRECTION ICI : on utilise .name au lieu de .subject_name
            messages.success(request, f"L'examen de {subject.name} a été programmé !")
            return redirect('exam_list')
        except (Subject.DoesNotExist, ValueError):
            messages.error(request, "Erreur : La matière sélectionnée est invalide.")

    subjects_list = Subject.objects.all()
    return render(request, 'exams/add_exam_form.html', {'subjects': subjects_list})

# 3. Supprimer un examen
@staff_member_required
def delete_exam_view(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    messages.warning(request, "Examen supprimé de la liste.")
    return redirect('exam_list')


# --- SECTION NOTES (MARKS) ---

# 4. Saisir les notes
@login_required(login_url='login') # Remplace 'login' par le nom de ton URL de connexion
def add_mark_view(request):
    # Sécurité : On vérifie si c'est un admin ou un prof
    # Si c'est un simple étudiant, on le renvoie ailleurs
    if not (request.user.is_staff or request.user.is_superuser or getattr(request.user, 'is_teacher', False)):
        messages.error(request, "Vous n'avez pas l'autorisation d'accéder à cette page.")
        return redirect('student_dashboard') # Ou ta page d'accueil

    if request.method == "POST":
        s_id = request.POST.get('student_id')
        e_id = request.POST.get('exam_id')
        score_val = request.POST.get('score')

        try:
            score = float(score_val.replace(',', '.'))
            if score < 0 or score > 20:
                messages.error(request, "La note doit être comprise entre 0 et 20.")
                return redirect('add_mark') # Utilise le nom exact de ton URL

            if Mark.objects.filter(student_id=s_id, exam_id=e_id).exists():
                messages.warning(request, "Cet étudiant possède déjà une note pour cet examen.")
            else:
                Mark.objects.create(student_id=s_id, exam_id=e_id, score=score)
                messages.success(request, f"Note de {score}/20 enregistrée avec succès !")
                return redirect('exam_list')

        except (ValueError, TypeError):
            messages.error(request, "Format de note invalide.")

    context = {
        'students': Student.objects.all().order_by('last_name'),
        'exams': Exam.objects.all().select_related('subject'),
    }
    return render(request, 'exams/add_results.html', context)

@login_required
def results_list_view(request):
    if request.user.is_staff or request.user.is_superuser:
        results = Mark.objects.all().select_related('student', 'exam', 'exam__subject')
    else:
        # Correction pour Hiba et les autres : student__user
        results = Mark.objects.filter(student__user=request.user).select_related('exam', 'exam__subject')
        
    # ATTENTION ICI : Dans ton image, le fichier s'appelle 'my_results.html'
    # Ton ancien code avait 'exams' tout court, ce qui faisait planter la page.
    return render(request, 'exams/my_results.html', {'results': results})