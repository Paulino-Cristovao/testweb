from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatbot_view, name='chatbot'),
    path('chat/history/', views.chat_history, name='chat_history'),
]