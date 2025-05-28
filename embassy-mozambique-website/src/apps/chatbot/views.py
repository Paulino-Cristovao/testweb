from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
import json
from .models import ChatSession, ChatMessage, KnowledgeBase
from .ai_service import ChatbotService

def chatbot_view(request):
    """Simple chatbot view function"""
    return render(request, 'chatbot/chat.html', {
        'title': 'Embassy Assistant'
    })

class ChatView(View):
    """Main chat interface"""
    template_name = 'chatbot/chat.html'
    
    def get(self, request):
        return render(request, self.template_name, {
            'title': 'Embassy Assistant'
        })

@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(View):
    """API endpoint for chat messages"""
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            session_id = data.get('session_id')
            
            # Get or create chat session
            if session_id:
                try:
                    session = ChatSession.objects.get(id=session_id)
                except ChatSession.DoesNotExist:
                    session = ChatSession.objects.create(
                        user=request.user if request.user.is_authenticated else None
                    )
            else:
                session = ChatSession.objects.create(
                    user=request.user if request.user.is_authenticated else None
                )
            
            # Save user message
            user_message = ChatMessage.objects.create(
                session=session,
                message_type='user',
                content=message
            )
            
            # Get bot response
            chatbot_service = ChatbotService()
            bot_response = chatbot_service.get_response(message, session)
            
            # Save bot message
            bot_message = ChatMessage.objects.create(
                session=session,
                message_type='bot',
                content=bot_response
            )
            
            return JsonResponse({
                'success': True,
                'session_id': str(session.id),
                'response': bot_response,
                'message_id': bot_message.id
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

@login_required
def chat_history(request):
    """View chat history for logged-in users"""
    sessions = ChatSession.objects.filter(user=request.user)
    return render(request, 'chatbot/history.html', {
        'sessions': sessions,
        'title': 'Chat History'
    })

@csrf_exempt
def chat_api(request):
    """Simple API endpoint for chat"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            # Simple response for now
            if not message:
                return JsonResponse({
                    'success': False,
                    'error': 'Message is required'
                }, status=400)
            
            # Create a basic response
            response = f"Thank you for your message: '{message}'. How can I help you further?"
            
            return JsonResponse({
                'success': True,
                'response': response
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST method allowed'
    }, status=405)

from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('api/chat/', views.ChatAPIView.as_view(), name='chat_api'),
    path('api/simple/', views.chat_api, name='simple_api'),
    path('history/', views.chat_history, name='history'),
]