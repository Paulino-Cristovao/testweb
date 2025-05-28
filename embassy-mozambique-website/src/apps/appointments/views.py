from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def appointment_list(request):
    return HttpResponse("<h1>Appointments</h1><p>Appointment system coming soon.</p>")

def booking_view(request):
    return HttpResponse("<h1>Book Appointment</h1><p>Online booking system coming soon.</p>")

@login_required
def my_appointments(request):
    return HttpResponse("<h1>My Appointments</h1><p>Your appointment history will appear here.</p>")
