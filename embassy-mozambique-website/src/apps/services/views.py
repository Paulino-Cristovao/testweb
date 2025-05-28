from django.shortcuts import render
from django.http import HttpResponse

def service_list(request):
    return HttpResponse("<h1>Embassy Services</h1><p>Service catalog coming soon.</p>")

def service_detail(request, service_id):
    return HttpResponse(f"<h1>Service Details</h1><p>Details for service {service_id} coming soon.</p>")
