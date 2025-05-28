from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.Model):
    """User roles for role-based access control"""
    ROLE_CHOICES = [
        ('citizen', 'Citizen'),
        ('staff', 'Embassy Staff'),
        ('admin', 'Administrator'),
    ]
    
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.get_name_display()

class User(AbstractUser):
    """Custom user model extending the default Django user model."""
    email = models.EmailField(unique=True)
    
    # Fix the reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
    def __str__(self):
        return self.email or self.username

class UserProfile(models.Model):
    """Extended user profile for embassy website users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    passport_number = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=100, default='Mozambican')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"