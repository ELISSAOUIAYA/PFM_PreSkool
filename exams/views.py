from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Exam, Mark
from subjects.models import Subject
from student.models import Student

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

    # --- LE LIEN AVEC LA BASE DE DONNÉES ---
    # On récupère toutes les matières. 
    # Ajoute un .order_by('name') pour être propre.
    subjects_list = Subject.objects.all()
    
    # Vérifie dans ta console si subjects_list contient quelque chose :
    print(f"DEBUG: Nombre de matières trouvées : {subjects_list.count()}")

    return render(request, 'exams/add_exam_form.html', {'subjects': subjects_list})

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
#
def add_mark_view(request):
    # Sécurité simple : On peut vérifier si l'utilisateur est admin
    if not request.user.is_staff:
        messages.error(request, "Accès refusé. Seuls les professeurs peuvent ajouter des notes.")
        return redirect('student_dashboard')

    if request.method == "POST":
        student_id = request.POST.get('student')
        exam_id = request.POST.get('exam')
        score = request.POST.get('score')
        remarks = request.POST.get('remarks')

        try:
            student = Student.objects.get(id=student_id)
            exam = Exam.objects.get(id=exam_id)
            
            Mark.objects.create(
                student=student,
                exam=exam,
                score=score,
                remarks=remarks
            )
            messages.success(request, "Note ajoutée avec succès !")
            return redirect('exam_list')
        except Exception as e:
            messages.error(request, f"Erreur : {e}")

    students = Student.objects.all()
    exams = Exam.objects.all()
    return render(request, 'exams/add_results.html', {
        'students': students, 
        'exams': exams
    })
def my_results_view(request):
    # On filtre les notes par l'utilisateur connecté
    # Note: Vérifie que ton modèle Student a un champ 'user' lié à Django User
    try:
        # On cherche l'étudiant lié à l'utilisateur actuel
        student_profile = Student.objects.get(first_name=request.user.username) # Adapté à ton modèle
        results = Mark.objects.filter(student=student_profile)
    except Student.DoesNotExist:
        results = []

    return render(request, 'exams/my_results.html', {'results': results})