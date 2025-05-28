from django import forms
from django.contrib.auth.models import User
from .models import Appointment, AppointmentSlot
from apps.services.models import Service

class AppointmentForm(forms.ModelForm):
    """Form for booking appointments"""
    
    class Meta:
        model = Appointment
        fields = [
            'service', 'appointment_date', 'appointment_time', 
            'notes', 'preferred_language'
        ]
        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': forms.DateInput().format_value(forms.DateInput().value_from_datadict({}, {}, 'today'))
                }
            ),
            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Any additional information or special requests...'
                }
            ),
            'preferred_language': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filter services that require appointments
        self.fields['service'].queryset = Service.objects.filter(
            appointment_required=True, 
            is_active=True
        )
        
        # Add CSS classes
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        from datetime import date
        
        if appointment_date < date.today():
            raise forms.ValidationError("Appointment date cannot be in the past.")
        
        return appointment_date

class AppointmentSlotForm(forms.ModelForm):
    """Form for creating appointment slots (admin use)"""
    
    class Meta:
        model = AppointmentSlot
        fields = ['date', 'start_time', 'end_time', 'max_appointments', 'is_available']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'max_appointments': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time.")
        
        return cleaned_data

class AppointmentUpdateForm(forms.ModelForm):
    """Form for updating appointment status (admin use)"""
    
    class Meta:
        model = Appointment
        fields = ['status', 'notes', 'admin_notes']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'admin_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AppointmentRescheduleForm(forms.ModelForm):
    """Form for rescheduling appointments"""
    
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        from datetime import date
        
        if appointment_date < date.today():
            raise forms.ValidationError("New appointment date cannot be in the past.")
        
        return appointment_date