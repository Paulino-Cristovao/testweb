from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

class Page(models.Model):
    """CMS Pages for the embassy website"""
    PAGE_TYPES = [
        ('static', 'Static Page'),
        ('news', 'News Article'),
        ('event', 'Event'),
        ('announcement', 'Announcement'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    page_type = models.CharField(max_length=20, choices=PAGE_TYPES, default='static')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    meta_description = models.TextField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('cms:page_detail', kwargs={'slug': self.slug})

class Content(models.Model):
    """Content blocks for pages"""
    CONTENT_TYPES = [
        ('text', 'Text Content'),
        ('html', 'HTML Content'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
        ('gallery', 'Image Gallery'),
    ]
    
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('pt', 'Portuguese'),
        ('fr', 'French'),
    ]
    
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='text')
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='cms/images/', blank=True, null=True)
    file = models.FileField(upload_to='cms/files/', blank=True, null=True)
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='en')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.page.title} - {self.title or self.content_type}"

class Menu(models.Model):
    """Navigation menu items"""
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    icon_class = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    """News articles for the embassy"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='news/images/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title