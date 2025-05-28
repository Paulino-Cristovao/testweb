from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Page, NewsArticle

class HomeView(TemplateView):
    template_name = 'cms/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Embassy of Mozambique in France'
        # Add any featured news or content here
        context['featured_news'] = []
        return context

def page_detail(request, slug):
    """Simple page detail view"""
    try:
        page = get_object_or_404(Page, slug=slug, status='published')
        return render(request, 'cms/page_detail.html', {'page': page})
    except:
        return HttpResponse(f"<h1>Page '{slug}' not found</h1><p><a href='/'>Go back to home</a></p>")

def news_list(request):
    """Simple news list view"""
    try:
        articles = NewsArticle.objects.filter(is_published=True)[:10]
        return render(request, 'cms/news_list.html', {'articles': articles})
    except:
        return HttpResponse("<h1>News</h1><p>No news articles available yet.</p><p><a href='/'>Go back to home</a></p>")
