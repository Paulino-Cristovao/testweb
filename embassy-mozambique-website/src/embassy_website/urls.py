from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.cms.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # Use CMS HomeView instead of apps.home
    path('accounts/', include('apps.accounts.urls')),
    path('appointments/', include('apps.appointments.urls')),
    path('services/', include('apps.services.urls')),
    path('documents/', include('apps.documents.urls')),
    path('chatbot/', include('apps.chatbot.urls')),
    path('cms/', include('apps.cms.urls')),
    path('auth/', include('allauth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "Embassy of Mozambique Administration"
admin.site.site_title = "Embassy Admin"
admin.site.index_title = "Welcome to Embassy Administration"