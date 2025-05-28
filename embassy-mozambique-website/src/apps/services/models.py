from django.db import models
from django.conf import settings

class ServiceCategory(models.Model):
    """Categories for embassy services"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # For CSS icon classes
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Service Categories"
    
    def __str__(self):
        return self.name

class Service(models.Model):
    """Embassy services model"""
    SERVICE_TYPES = [
        ('visa', 'Visa Services'),
        ('passport', 'Passport Services'),
        ('consular', 'Consular Services'),
        ('notarial', 'Notarial Services'),
        ('emergency', 'Emergency Services'),
        ('business', 'Business Services'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    requirements = models.TextField(help_text="List of required documents")
    processing_time = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    is_active = models.BooleanField(default=True)
    appointment_required = models.BooleanField(default=True)
    online_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.category}"

class ServiceRequest(models.Model):
    """Service requests from users"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.service.name}"