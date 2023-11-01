import os
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Configure as credenciais da API do ChatGPT
openai.api_key = os.getenv("OPENAI_API_KEY")

# Página inicial com o formulário de chat
@app.route("/")
def home():
    return render_template("index.html")

# Rota para lidar com mensagens do visitante e gerar respostas do ChatGPT
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]

    # Chame a API do ChatGPT para obter uma resposta
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        max_tokens=50
    )

    bot_response = response.choices[0].text

    return bot_response

if __name__ == "__main__":
    app.run()
