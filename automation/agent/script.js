import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/chat.bundle.es.js';

document.addEventListener("DOMContentLoaded", () => {
  const chat = createChat({
    webhookUrl: "https://f0e6d2ba353b.ngrok-free.app/webhook/5d502fa9-20a9-4d71-9d87-cdb38f612043/chat",
    target: "#n8n-chat",
    loadPreviousSession: false,
    enableStreaming: true,
    defaultLanguage: 'en',
    showWelcomeScreen: false,
    mode: 'window',
	chatInputKey: 'chatInput',
	chatSessionKey: 'sessionId',
	initialMessages: [
		'Hi there! 👋',
		'My name is Matilda. How can I assist you today?'
	],
    i18n: {
		en: {
			title: 'Bonjour! 👋',
			subtitle: "What would like to know about the Regreening app?",
			footer: '',
			getStarted: 'New Conversation',
			inputPlaceholder: 'Type your question..',
		},
	},
    });
});
