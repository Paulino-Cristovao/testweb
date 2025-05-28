from django.contrib import admin
from .models import UserProfile, UserRole

admin.site.register(UserProfile)
admin.site.register(UserRole)