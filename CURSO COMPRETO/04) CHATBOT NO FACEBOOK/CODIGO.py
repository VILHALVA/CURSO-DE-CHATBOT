from pymessenger.bot import Bot

# Defina as credenciais do seu aplicativo no Facebook
ACCESS_TOKEN = 'seu_token_de_acesso'
VERIFY_TOKEN = 'seu_token_de_verificação'

# Crie uma instância do bot
bot = Bot(ACCESS_TOKEN)

# Função para processar mensagens de entrada
def process_message(event):
    user_id = event['sender']['id']
    message_text = event['message']['text']

    # Lógica do chatbot: responda à mensagem do usuário
    response = f"Você disse: '{message_text}'"

    # Envie a resposta de volta ao usuário
    bot.send_text_message(user_id, response)

# Função para verificar mensagens de entrada
def verify_fb_token(token_sent):
    return token_sent == VERIFY_TOKEN

# Rota para receber mensagens do Facebook
@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verificação do token
        token_sent = request.args.get("hub.verify_token")
        if verify_fb_token(token_sent):
            return request.args.get("hub.challenge")
        return 'Token de verificação inválido'
    else:
        # Processar mensagens de entrada
        data = request.get_json()
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    process_message(messaging_event)
        return "Mensagem recebida"

if __name__ == "__main__":
    app.run()
