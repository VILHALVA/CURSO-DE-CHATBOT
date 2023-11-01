from instabot import Bot

# Crie uma instância do bot
bot = Bot()

# Faça login na sua conta do Instagram
bot.login(username='seu_usuario', password='sua_senha')

# Função para responder a mensagens diretas
def responder_dm(username, message):
    # Envie uma mensagem de volta para o usuário
    bot.send_message(message, [username])

# Inicie um loop para verificar e responder a mensagens
while True:
    # Obtenha novas mensagens diretas
    new_messages = bot.get_all_messages()
    
    for message in new_messages:
        sender = message['user']
        message_text = message['text']
        
        # Lógica para responder à mensagem (personalize conforme necessário)
        resposta = f"Obrigado por sua mensagem: {message_text}"
        
        # Responda à mensagem
        responder_dm(sender, resposta)
