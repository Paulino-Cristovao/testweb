from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list, name='list'),
    path('book/', views.booking_view, name='booking'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
]
