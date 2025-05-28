from django.db import models
from django.conf import settings
from apps.services.models import Service
import uuid
import os

def upload_to(instance, filename):
    """Generate upload path for documents"""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('documents', str(instance.user.id), filename)

class DocumentType(models.Model):
    """Types of documents that can be uploaded"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    required_for_services = models.ManyToManyField(Service, blank=True)
    is_required = models.BooleanField(default=False)
    max_file_size = models.IntegerField(default=5242880)  # 5MB in bytes
    allowed_extensions = models.CharField(max_length=200, default='pdf,jpg,jpeg,png')
    
    def __str__(self):
        return self.name

class Document(models.Model):
    """User uploaded documents"""
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_to)
    file_size = models.IntegerField(default=0)
    mime_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='reviewed_documents'
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

class DocumentTemplate(models.Model):
    """Document templates for download"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='templates/')
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    language = models.CharField(max_length=5, choices=[
        ('en', 'English'),
        ('pt', 'Portuguese'), 
        ('fr', 'French'),
    ], default='en')
    version = models.CharField(max_length=10, default='1.0')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} v{self.version}"