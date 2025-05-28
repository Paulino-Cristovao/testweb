/**
 * Embassy of Mozambique Website - Chatbot Integration
 * AI-powered multilingual assistant
 */

// Professional Embassy Chatbot - White & Red Theme

class EmbassyChatbot {
    constructor() {
        this.isOpen = false;
        this.messages = [];
        this.init();
    }

    init() {
        this.createChatbotHTML();
        this.bindEvents();
        this.addWelcomeMessage();
    }

    createChatbotHTML() {
        const chatbotHTML = `
            <div class="chatbot-widget" id="chatbotWidget">
                <div class="chatbot-button" id="chatbotButton">
                    <i class="fas fa-comments"></i>
                    <span class="chatbot-notification" id="chatbotNotification">1</span>
                </div>
                
                <div class="chatbot-window" id="chatbotWindow">
                    <div class="chatbot-header">
                        <div class="d-flex align-items-center">
                            <div class="chatbot-avatar me-2">
                                <i class="fas fa-robot"></i>
                            </div>
                            <div>
                                <h6 class="mb-0">Assistente da Embaixada</h6>
                                <small style="color: rgba(255,255,255,0.8);">Online - Pronto para ajudar</small>
                            </div>
                        </div>
                        <button class="btn btn-sm btn-link text-white p-0" id="chatbotClose">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    
                    <div class="chatbot-messages" id="chatbotMessages">
                        <!-- Messages will be added here -->
                    </div>
                    
                    <div class="chatbot-input">
                        <div class="input-group">
                            <input type="text" class="form-control" id="chatbotInput" placeholder="Escreva a sua mensagem...">
                            <button class="btn btn-primary" type="button" id="chatbotSend">
                                <i class="fas fa-paper-plane"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
    }

    bindEvents() {
        const button = document.getElementById('chatbotButton');
        const closeBtn = document.getElementById('chatbotClose');
        const sendBtn = document.getElementById('chatbotSend');
        const input = document.getElementById('chatbotInput');

        button.addEventListener('click', () => this.toggle());
        closeBtn.addEventListener('click', () => this.close());
        sendBtn.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
    }

    toggle() {
        if (this.isOpen) {
            this.close();
        } else {
            this.open();
        }
    }

    open() {
        const window = document.getElementById('chatbotWindow');
        const notification = document.getElementById('chatbotNotification');
        
        window.style.display = 'flex';
        notification.style.display = 'none';
        this.isOpen = true;
        
        // Focus input
        setTimeout(() => {
            document.getElementById('chatbotInput').focus();
        }, 300);
    }

    close() {
        const window = document.getElementById('chatbotWindow');
        window.style.display = 'none';
        this.isOpen = false;
    }

    sendMessage() {
        const input = document.getElementById('chatbotInput');
        const message = input.value.trim();
        
        if (!message) return;

        this.addUserMessage(message);
        input.value = '';
        
        // Simulate bot response
        setTimeout(() => {
            this.handleBotResponse(message);
        }, 1000);
    }

    addUserMessage(message) {
        const messagesContainer = document.getElementById('chatbotMessages');
        const messageHTML = `
            <div class="message user-message">
                <div class="avatar">
                    <i class="fas fa-user"></i>
                </div>
                <div class="content">
                    <p class="mb-0">${message}</p>
                </div>
            </div>
        `;
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        this.scrollToBottom();
    }

    addBotMessage(message, quickActions = []) {
        const messagesContainer = document.getElementById('chatbotMessages');
        let quickActionsHTML = '';
        
        if (quickActions.length > 0) {
            quickActionsHTML = '<div class="quick-actions mt-2">';
            quickActions.forEach(action => {
                quickActionsHTML += `<button class="btn btn-outline-primary btn-sm me-1 mb-1" onclick="chatbot.handleQuickAction('${action.action}')">${action.label}</button>`;
            });
            quickActionsHTML += '</div>';
        }

        const messageHTML = `
            <div class="message bot-message">
                <div class="avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="content">
                    <p class="mb-0">${message}</p>
                    ${quickActionsHTML}
                </div>
            </div>
        `;
        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        this.scrollToBottom();
    }

    addWelcomeMessage() {
        const welcomeMessage = "Olá! Sou o assistente virtual da Embaixada de Moçambique em França. Como posso ajudá-lo hoje?";
        const quickActions = [
            { label: "Agendar Consulta", action: "appointment" },
            { label: "Serviços", action: "services" },
            { label: "Horários", action: "hours" },
            { label: "Contactos", action: "contact" }
        ];
        
        setTimeout(() => {
            this.addBotMessage(welcomeMessage, quickActions);
        }, 500);
    }

    handleBotResponse(userMessage) {
        const message = userMessage.toLowerCase();
        let response = "";
        let quickActions = [];

        if (message.includes("agendar") || message.includes("consulta") || message.includes("appointment")) {
            response = "Para agendar uma consulta, pode escolher uma das seguintes opções:";
            quickActions = [
                { label: "Passaporte", action: "passport" },
                { label: "Bilhete ID", action: "id" },
                { label: "Visto", action: "visa" },
                { label: "Outros Serviços", action: "other_services" }
            ];
        } else if (message.includes("passaporte") || message.includes("passport")) {
            response = "Para serviços de passaporte, precisará dos seguintes documentos:\n\n• Bilhete de identidade\n• 2 fotografias recentes\n• Formulário preenchido\n• Comprovativo de pagamento\n\nProcessamento: 15-20 dias úteis\nTaxa: €80";
            quickActions = [
                { label: "Agendar Passaporte", action: "book_passport" },
                { label: "Mais Informações", action: "passport_info" }
            ];
        } else if (message.includes("visto") || message.includes("visa")) {
            response = "Oferecemos os seguintes tipos de visto:\n\n• Visto de Turismo\n• Visto de Negócios\n• Visto de Trabalho\n• Visto de Trânsito\n\nProcessamento: 5-10 dias úteis\nTaxas variam entre €50-€150";
            quickActions = [
                { label: "Agendar Visto", action: "book_visa" },
                { label: "Tipos de Visto", action: "visa_types" }
            ];
        } else if (message.includes("bilhete") || message.includes("identidade") || message.includes("id")) {
            response = "Para emissão/renovação de Bilhete de Identidade:\n\n• Certidão de nascimento\n• 2 fotografias recentes\n• Comprovativo de residência\n• Bilhete anterior (se renovação)\n\nProcessamento: 10-15 dias úteis\nTaxa: €60";
            quickActions = [
                { label: "Agendar BI", action: "book_id" },
                { label: "Documentos Necessários", action: "id_docs" }
            ];
        } else if (message.includes("horário") || message.includes("hours") || message.includes("funcionamento")) {
            response = "Horário de Atendimento:\n\n🕘 Segunda a Sexta: 9:00 - 17:00\n🕘 Sábado: 9:00 - 13:00\n🕘 Domingo: Fechado\n\n📞 Emergências 24h: +33 (0) 6 XX XX XX XX";
            quickActions = [
                { label: "Agendar Consulta", action: "appointment" },
                { label: "Contacto Emergência", action: "emergency" }
            ];
        } else if (message.includes("contacto") || message.includes("contact") || message.includes("telefone")) {
            response = "Contactos da Embaixada:\n\n📍 Endereço: Embassy Address, Paris\n📞 Telefone: +33 (0) 1 XX XX XX XX\n📧 Email: info@mozambique-embassy.fr\n🚨 Emergência 24h: +33 (0) 6 XX XX XX XX";
            quickActions = [
                { label: "Ver no Mapa", action: "map" },
                { label: "Enviar Email", action: "email" }
            ];
        } else if (message.includes("emergência") || message.includes("emergency") || message.includes("urgente")) {
            response = "Para emergências, contacte imediatamente:\n\n🚨 Linha de Emergência 24h\n📞 +33 (0) 6 XX XX XX XX\n\nPara que tipo de emergência precisa de assistência?";
            quickActions = [
                { label: "Ligar Agora", action: "call_emergency" },
                { label: "Assistência Médica", action: "medical" },
                { label: "Documento Perdido", action: "lost_doc" }
            ];
        } else {
            response = "Obrigado pela sua mensagem. Posso ajudá-lo com informações sobre:";
            quickActions = [
                { label: "Serviços Consulares", action: "services" },
                { label: "Agendamentos", action: "appointment" },
                { label: "Contactos", action: "contact" },
                { label: "Emergências", action: "emergency" }
            ];
        }

        this.addBotMessage(response, quickActions);
    }

    handleQuickAction(action) {
        switch (action) {
            case "appointment":
                this.addUserMessage("Quero agendar uma consulta");
                setTimeout(() => this.handleBotResponse("agendar consulta"), 500);
                break;
            case "services":
                this.addUserMessage("Que serviços estão disponíveis?");
                setTimeout(() => {
                    this.addBotMessage("Os nossos principais serviços incluem:", [
                        { label: "Passaporte", action: "passport" },
                        { label: "Bilhete de Identidade", action: "id" },
                        { label: "Vistos", action: "visa" },
                        { label: "Registos e Notariais", action: "notarial" }
                    ]);
                }, 500);
                break;
            case "passport":
                this.addUserMessage("Informações sobre passaporte");
                setTimeout(() => this.handleBotResponse("passaporte"), 500);
                break;
            case "visa":
                this.addUserMessage("Informações sobre vistos");
                setTimeout(() => this.handleBotResponse("visto"), 500);
                break;
            case "id":
                this.addUserMessage("Informações sobre bilhete de identidade");
                setTimeout(() => this.handleBotResponse("bilhete identidade"), 500);
                break;
            case "hours":
                this.addUserMessage("Qual é o horário de funcionamento?");
                setTimeout(() => this.handleBotResponse("horário"), 500);
                break;
            case "contact":
                this.addUserMessage("Como posso contactar a embaixada?");
                setTimeout(() => this.handleBotResponse("contacto"), 500);
                break;
            case "emergency":
                this.addUserMessage("Preciso de assistência de emergência");
                setTimeout(() => this.handleBotResponse("emergência"), 500);
                break;
            case "book_passport":
            case "book_visa":
            case "book_id":
                this.addBotMessage("Para agendar, pode usar o botão 'Agendar Consulta' no topo da página ou ligar para +33 (0) 1 XX XX XX XX durante o horário de atendimento.");
                break;
            case "call_emergency":
                window.open("tel:+33123456789", "_self");
                break;
            default:
                this.addBotMessage("Como posso ajudá-lo?", [
                    { label: "Serviços", action: "services" },
                    { label: "Agendar", action: "appointment" },
                    { label: "Contactos", action: "contact" }
                ]);
        }
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbotMessages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}

// Initialize chatbot when page loads
document.addEventListener('DOMContentLoaded', function() {
    window.chatbot = new EmbassyChatbot();
});

// Make chatbot globally available
window.openChatbot = function() {
    if (window.chatbot) {
        window.chatbot.open();
    }
};