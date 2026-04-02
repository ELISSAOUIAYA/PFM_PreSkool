from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Holiday


@login_required
def holiday_list(request):
    """Affiche la liste de tous les jours fériés"""
    holidays = Holiday.objects.all()
    context = {'holidays': holidays}
    return render(request, 'holidays/holiday_list.html', context)


@login_required
def holiday_detail(request, pk):
    """Affiche les détails d'un jour férié"""
    holiday = get_object_or_404(Holiday, pk=pk)
    context = {'holiday': holiday}
    return render(request, 'holidays/holiday_detail.html', context)


@login_required
def holiday_create(request):
    """Crée un nouveau jour férié"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        is_national_holiday = request.POST.get('is_national_holiday') == 'on'
        
        holiday = Holiday.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            is_national_holiday=is_national_holiday
        )
        return redirect('holiday-detail', pk=holiday.pk)
    
    context = {}
    return render(request, 'holidays/holiday_form.html', context)


@login_required
def holiday_update(request, pk):
    """Modifie un jour férié existant"""
    holiday = get_object_or_404(Holiday, pk=pk)
    
    if request.method == 'POST':
        holiday.name = request.POST.get('name')
        holiday.description = request.POST.get('description')
        holiday.start_date = request.POST.get('start_date')
        holiday.end_date = request.POST.get('end_date')
        holiday.is_national_holiday = request.POST.get('is_national_holiday') == 'on'
        holiday.save()
        return redirect('holiday-detail', pk=holiday.pk)
    
    context = {'holiday': holiday}
    return render(request, 'holidays/holiday_form.html', context)


@login_required
def holiday_delete(request, pk):
    """Supprime un jour férié"""
    holiday = get_object_or_404(Holiday, pk=pk)
    
    if request.method == 'POST':
        holiday.delete()
        return redirect('holiday-list')
    
    context = {'holiday': holiday}
    return render(request, 'holidays/holiday_confirm_delete.html', context)
