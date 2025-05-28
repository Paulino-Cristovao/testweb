from django.contrib import admin
from .models import DocumentType, Document, DocumentTemplate

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_required', 'max_file_size']
    list_filter = ['is_required']
    search_fields = ['name', 'description']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'document_type', 'status', 'uploaded_at']
    list_filter = ['status', 'document_type', 'uploaded_at']
    search_fields = ['title', 'user__username', 'user__email']

@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'document_type', 'language', 'version', 'is_active']
    list_filter = ['document_type', 'language', 'is_active']
    search_fields = ['name', 'description']