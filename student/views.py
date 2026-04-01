from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Mark
from holidays.models import Holiday
from subjects.models import Subject
from student.models import Student , Parent
from django.contrib import messages

def student_list(request):

    students = Student.objects.all()
    
    count_students = students.count()
    
    context = {
        'students': students,
        'count_students': count_students,
    }
    return render(request, 'students/students.html', context)

def add_student(request):
 if request.method == 'POST':
# Récupérer les données de l'étudiant
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
# Récupérer les données du parent
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
# Créer l'objet Parent
        parent = Parent.objects.create(
        father_name=father_name,
        father_occupation=father_occupation,
        father_mobile=father_mobile,
        father_email=father_email,
        mother_name=mother_name,
        mother_occupation=mother_occupation,
        mother_mobile=mother_mobile,
        mother_email=mother_email,
        present_address=present_address,
        permanent_address=permanent_address
)
# Créer l'objet Student
        student = Student.objects.create(
         first_name=first_name,
         last_name=last_name,
         student_id=student_id,
         gender=gender,
         date_of_birth=date_of_birth,
         student_class=student_class,
         joining_date=joining_date,
         mobile_number=mobile_number,
         admission_number=admission_number,
         section=section,
         student_image=student_image,
         parent=parent
)
        messages.success(request, 'Student added Successfully')
        return redirect('student_list')
 else:
   return render(request, 'students/add-student.html')
        

# 1. Le Dashboard Étudiant
@login_required
def student_dashboard(request):
    username = request.user.username
    context = {
        'timetables': [], 
        'upcoming_exams': Exam.objects.order_by('date')[:3],
        'latest_results': Mark.objects.filter(student__first_name=username).order_by('-id')[:5],
        'holidays': Holiday.objects.all().order_by('start_date')[:3],
        'my_subjects': Subject.objects.all(),
    }
    return render(request, 'students/student-dashboard.html', context)

# 2. Voir un étudiant spécifique (C'est celle qui manquait !)
def view_student(request, student_id):
    # Pour l'instant, on renvoie juste vers le template
    return render(request, 'student/view_student.html', {'id': student_id})

# 3. Ajouter un étudiant
def add_student(request):
    return render(request, 'student/add_student.html')

# 4. Liste des étudiants
def student_list(request):
    return render(request, 'student/student_list.html')

# 5. Modifier un étudiant
def edit_student(request, pk):
    return render(request, 'student/edit_student.html')

# 6. Supprimer un étudiant
def delete_student(request, pk):
    return redirect('student_list')