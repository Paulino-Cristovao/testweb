from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Page, NewsArticle

class HomeView(TemplateView):
    template_name = 'cms/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Embassy of Mozambique in France',
            'page_description': 'Official website of the Embassy of Mozambique in France - Consular services, visa information, and assistance for Mozambican citizens.',
            'ambassador_message': {
                'title': 'Mensagem da Embaixadora',
                'content': 'Bem-vindos ao website oficial da Embaixada de Moçambique em França. É com grande prazer que vos damos as boas-vindas a este espaço digital onde poderão encontrar informações úteis sobre os nossos serviços consulares.',
                'name': 'Sua Excelência Dr.ª Maria João Santos',
                'position': 'Embaixadora de Moçambique em França'
            },
            'recent_news': self.get_recent_news(),
            'important_links': self.get_important_links(),
            'office_hours': {
                'weekdays': 'Segunda a Sexta: 9:00 - 17:00',
                'saturday': 'Sábado: 9:00 - 13:00',
                'closed': 'Domingo: Fechado'
            }
        })
        return context
    
    def get_recent_news(self):
        """Get recent news articles"""
        try:
            return NewsArticle.objects.filter(is_published=True)[:3]
        except:
            return []
    
    def get_important_links(self):
        """Get important external links"""
        return [
            {
                'title': 'Visit Mozambique',
                'url': 'https://www.visitmozambique.net',
                'description': 'Portal oficial de turismo de Moçambique',
                'icon': 'fas fa-map'
            },
            {
                'title': 'Finanças de Moçambique',
                'url': 'https://www.mf.gov.mz',
                'description': 'Ministério das Finanças',
                'icon': 'fas fa-euro-sign'
            },
            {
                'title': 'Segurança Social',
                'url': 'https://www.inss.gov.mz',
                'description': 'Instituto Nacional de Segurança Social',
                'icon': 'fas fa-shield-alt'
            },
            {
                'title': 'Portal do Governo',
                'url': 'https://www.portaldogoverno.gov.mz',
                'description': 'Portal oficial do Governo de Moçambique',
                'icon': 'fas fa-landmark'
            }
        ]

def page_detail(request, slug):
    """Enhanced page detail view"""
    try:
        page = get_object_or_404(Page, slug=slug, status='published')
        context = {
            'page': page,
            'breadcrumbs': [
                {'title': 'Início', 'url': '/'},
                {'title': page.title, 'url': None}
            ]
        }
        return render(request, 'cms/page_detail.html', context)
    except Page.DoesNotExist:
        return render(request, 'cms/404.html', {
            'error_message': f"A página '{slug}' não foi encontrada.",
            'suggestions': [
                {'title': 'Voltar ao Início', 'url': '/'},
                {'title': 'Serviços Consulares', 'url': '#services'},
                {'title': 'Contacto', 'url': '#contact'}
            ]
        }, status=404)

def news_list(request):
    """Enhanced news list view"""
    try:
        articles = NewsArticle.objects.filter(is_published=True).order_by('-created_at')
        
        # Pagination
        from django.core.paginator import Paginator
        paginator = Paginator(articles, 6)  # Show 6 articles per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'articles': page_obj,
            'page_obj': page_obj,
            'total_articles': paginator.count,
            'breadcrumbs': [
                {'title': 'Início', 'url': '/'},
                {'title': 'Notícias e Eventos', 'url': None}
            ]
        }
        return render(request, 'cms/news_list.html', context)
    except Exception as e:
        return render(request, 'cms/news_list.html', {
            'articles': [],
            'error_message': 'Não há notícias disponíveis no momento.',
            'breadcrumbs': [
                {'title': 'Início', 'url': '/'},
                {'title': 'Notícias e Eventos', 'url': None}
            ]
        })

def contact_view(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        from django.contrib import messages
        messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contacto brevemente.')
    
    context = {
        'contact_info': {
            'address': 'Embassy Address, Paris, France',
            'phone': '+33 (0) 1 XX XX XX XX',
            'email': 'info@mozambique-embassy.fr',
            'emergency': '+33 (0) 6 XX XX XX XX',
            'hours': {
                'weekdays': 'Segunda a Sexta: 9:00 - 17:00',
                'saturday': 'Sábado: 9:00 - 13:00',
                'sunday': 'Domingo: Fechado'
            }
        },
        'breadcrumbs': [
            {'title': 'Início', 'url': '/'},
            {'title': 'Contacto', 'url': None}
        ]
    }
    return render(request, 'cms/contact.html', context)
