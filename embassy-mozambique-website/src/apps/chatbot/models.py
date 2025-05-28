from django.db import models
from django.conf import settings
import uuid

class ChatSession(models.Model):
    """Chat session model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Chat Session {self.id}"

class ChatMessage(models.Model):
    """Individual chat messages"""
    MESSAGE_TYPES = [
        ('user', 'User Message'),
        ('bot', 'Bot Message'),
        ('system', 'System Message'),
    ]
    
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    content = models.TextField()
    metadata = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.message_type}: {self.content[:50]}..."

class KnowledgeBase(models.Model):
    """Knowledge base for chatbot responses"""
    CONTENT_TYPES = [
        ('faq', 'FAQ'),
        ('procedure', 'Procedure'),
        ('requirement', 'Requirement'),
        ('general', 'General Information'),
    ]
    
    title = models.CharField(max_length=200)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    content = models.TextField()
    keywords = models.TextField(help_text="Comma-separated keywords")
    language = models.CharField(max_length=5, choices=[
        ('en', 'English'),
        ('pt', 'Portuguese'),
        ('fr', 'French'),
    ], default='en')
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority', 'title']
    
    def __str__(self):
        return self.title