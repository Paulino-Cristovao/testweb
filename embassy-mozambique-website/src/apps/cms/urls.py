from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/', views.news_list, name='news_list'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
