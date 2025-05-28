from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.document_list, name='list'),
    path('templates/', views.document_templates, name='templates'),
    path('upload/', views.document_upload, name='upload'),
]
