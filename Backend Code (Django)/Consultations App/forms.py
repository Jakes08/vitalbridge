from django import forms
from .models import Appointment, ConsultationFeedback
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role='doctor'))
    
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ConsultationFeedback
        fields = ['rating', 'comments']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }
