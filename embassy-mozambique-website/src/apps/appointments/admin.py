from django.contrib import admin
from .models import Appointment, AppointmentSlot

@admin.register(AppointmentSlot)
class AppointmentSlotAdmin(admin.ModelAdmin):
    list_display = ['date', 'start_time', 'end_time', 'max_appointments', 'is_available']
    list_filter = ['is_available', 'date']
    search_fields = ['date']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'appointment_date', 'appointment_time', 'status', 'created_at']
    list_filter = ['status', 'appointment_date', 'service']
    search_fields = ['user__username', 'user__email', 'service__name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'service', 'appointment_date', 'appointment_time')
        }),
        ('Status', {
            'fields': ('status', 'preferred_language')
        }),
        ('Notes', {
            'fields': ('notes', 'admin_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'confirmed_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user', 'service')