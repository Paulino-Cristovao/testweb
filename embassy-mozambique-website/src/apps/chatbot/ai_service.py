from django.conf import settings
import openai
from .models import KnowledgeBase
import re

class ChatbotService:
    """AI-powered chatbot service"""
    
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.knowledge_base = self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """Load knowledge base content"""
        kb_items = KnowledgeBase.objects.filter(is_active=True)
        knowledge = {}
        
        for item in kb_items:
            keywords = [kw.strip().lower() for kw in item.keywords.split(',')]
            knowledge[item.title] = {
                'content': item.content,
                'keywords': keywords,
                'type': item.content_type
            }
        
        return knowledge
    
    def _find_relevant_info(self, message):
        """Find relevant information from knowledge base"""
        message_lower = message.lower()
        relevant_items = []
        
        for title, info in self.knowledge_base.items():
            for keyword in info['keywords']:
                if keyword in message_lower:
                    relevant_items.append(info['content'])
                    break
        
        return relevant_items[:3]  # Return top 3 relevant items
    
    def get_response(self, message, session=None):
        """Generate chatbot response"""
        # First, try to find relevant information from knowledge base
        relevant_info = self._find_relevant_info(message)
        
        if relevant_info:
            # Use knowledge base information
            context = "\n".join(relevant_info)
            return self._generate_contextual_response(message, context)
        else:
            # Use general embassy information
            return self._generate_general_response(message)
    
    def _generate_contextual_response(self, message, context):
        """Generate response using OpenAI with context"""
        if not settings.OPENAI_API_KEY:
            return self._fallback_response(message)
        
        try:
            prompt = f"""
            You are an AI assistant for the Embassy of Mozambique in France. 
            Use the following context to answer the user's question:
            
            Context: {context}
            
            User Question: {message}
            
            Provide a helpful, accurate response based on the context. If the context doesn't contain enough information, politely explain what you can help with and suggest contacting the embassy directly.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful embassy assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return self._fallback_response(message)
    
    def _generate_general_response(self, message):
        """Generate general response"""
        if not settings.OPENAI_API_KEY:
            return self._fallback_response(message)
        
        try:
            prompt = f"""
            You are an AI assistant for the Embassy of Mozambique in France. 
            The user asked: {message}
            
            Provide a helpful response about embassy services, visa information, or direct them to contact the embassy for specific assistance.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful embassy assistant for the Embassy of Mozambique in France."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=250,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return self._fallback_response(message)
    
    def _fallback_response(self, message):
        """Fallback response when AI is not available"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['visa', 'visas']):
            return """For visa information, please visit our Services section or contact the embassy directly. 
            We offer tourist, business, and other types of visas. Each has specific requirements and processing times."""
        
        elif any(word in message_lower for word in ['passport', 'passports']):
            return """For passport services including renewals and new applications, please book an appointment through our online system. 
            Required documents and fees are listed in our Services section."""
        
        elif any(word in message_lower for word in ['appointment', 'booking']):
            return """You can book an appointment through our online appointment system. 
            Please select the service you need and choose an available time slot."""
        
        elif any(word in message_lower for word in ['contact', 'phone', 'address']):
            return """You can contact us at:
            Embassy of Mozambique in France
            [Address and contact information]
            
            For urgent matters, please use our emergency contact service."""
        
        else:
            return """Hello! I'm here to help with information about embassy services. 
            You can ask me about visas, passports, appointments, or general embassy information. 
            For specific assistance, please contact the embassy directly."""