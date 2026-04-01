from django import forms
from .models import TimeTable

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['subject', 'teacher', 'day_of_week', 'start_time', 'end_time', 'room']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Salle 101'}),
        }