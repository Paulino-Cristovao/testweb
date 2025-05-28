from django.contrib import admin
from .models import Content, Page

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'slug')

admin.site.register(Content, ContentAdmin)
admin.site.register(Page, PageAdmin)