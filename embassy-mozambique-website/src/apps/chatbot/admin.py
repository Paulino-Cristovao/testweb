from django.contrib import admin
from .models import ChatSession, ChatMessage, KnowledgeBase

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__username', 'user__email']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['session', 'message_type', 'content_preview', 'timestamp']
    list_filter = ['message_type', 'timestamp']
    search_fields = ['content']
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_type', 'language', 'is_active', 'priority']
    list_filter = ['content_type', 'language', 'is_active']
    search_fields = ['title', 'content', 'keywords']