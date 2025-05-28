from django.db import models
from django.conf import settings
from apps.services.models import Service
from datetime import datetime, date

class AppointmentSlot(models.Model):
    """Available time slots for appointments"""
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_appointments = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['date', 'start_time']
        ordering = ['date', 'start_time']
    
    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"
    
    @property
    def available_spots(self):
        booked_count = self.appointments.filter(
            status__in=['confirmed', 'pending']
        ).count()
        return self.max_appointments - booked_count

class Appointment(models.Model):
    """Appointment booking model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ('no_show', 'No Show'),
    ]
    
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('pt', 'Portuguese'),
        ('fr', 'French'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, help_text="User notes or special requests")
    admin_notes = models.TextField(blank=True, help_text="Internal admin notes")
    preferred_language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='en')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
        unique_together = ['user', 'appointment_date', 'appointment_time']
    
    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.appointment_date}"
    
    @property
    def is_past_due(self):
        appointment_datetime = datetime.combine(self.appointment_date, self.appointment_time)
        return appointment_datetime < datetime.now()
    
    def can_be_cancelled(self):
        """Check if appointment can be cancelled (not past and not completed)"""
        return not self.is_past_due and self.status not in ['completed', 'cancelled']