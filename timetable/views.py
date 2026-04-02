from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeTable
from .forms import TimeTableForm

def timetable_list(request):
    items = TimeTable.objects.all().order_by('day_of_week', 'start_time')
    return render(request, 'timetable/timetable_list.html', {'timetables': items})

def timetable_add(request):
    if request.method == "POST":
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimeTableForm()
    return render(request, 'timetable/timetable_form.html', {'form': form, 'title': 'Ajouter'})

def timetable_edit(request, pk):
    instance = get_object_or_404(TimeTable, pk=pk)
    if request.method == "POST":
        form = TimeTableForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimeTableForm(instance=instance)
    return render(request, 'timetable/timetable_form.html', {'form': form, 'title': 'Modifier'})