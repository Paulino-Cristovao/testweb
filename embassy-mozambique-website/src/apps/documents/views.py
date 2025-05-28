from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def document_list(request):
    return HttpResponse("<h1>Documents</h1><p>Document management coming soon.</p>")

def document_templates(request):
    return HttpResponse("<h1>Document Templates</h1><p>Download forms and templates here.</p>")

@login_required
def document_upload(request):
    return HttpResponse("<h1>Upload Documents</h1><p>Document upload feature coming soon.</p>")
