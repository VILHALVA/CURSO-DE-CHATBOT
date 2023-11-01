# SEU PRIMEIRO CHATBOT
Vou lhe dar uma introdução básica sobre como criar um chatbot simples em Python. Para criar um chatbot inteligente, você precisará de um conjunto de bibliotecas e serviços, e também é importante definir o escopo e os objetivos do seu chatbot. Neste exemplo, usaremos a biblioteca `nltk` para processamento de linguagem natural e o módulo `re` para expressões regulares. Aqui está um exemplo básico:

**Passo 1: Instalar as bibliotecas necessárias**

Certifique-se de ter o Python instalado e instale as bibliotecas `nltk` e `re` se ainda não as tiver:

```bash
pip install nltk
```

**Passo 2: Importar as bibliotecas e configurar o chatbot**

```python
import nltk
import re
import random

# Faça o download de recursos necessários do NLTK
nltk.download('punkt')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Defina padrões de saudação e despedida
saudacoes = ['olá', 'oi', 'e aí', 'olá!', 'oi!']
despedidas = ['tchau', 'adeus', 'até logo', 'até mais', 'tchau!']

# Dicionário de respostas
respostas = {
    'como você está?': ['Estou bem, obrigado!', 'Tudo tranquilo!', 'Nada mal, e você?'],
    'qual é o seu nome?': ['Meu nome é ChatGPT!', 'Sou o ChatGPT, e você?'],
    'ajuda': ['Como posso ajudar você?', 'Em que posso ajudar?', 'Pergunte-me qualquer coisa.'],
    'bom dia': ['Bom dia!', 'Dia bom!', 'Olá!'],
    'boa tarde': ['Boa tarde!', 'Tarde boa!', 'Olá!'],
    'boa noite': ['Boa noite!', 'Noite boa!', 'Olá!'],
}

# Função para responder a perguntas
def responder(pergunta):
    for padrao, respostas_possiveis in respostas.items():
        if re.search(padrao, pergunta.lower()):
            return random.choice(respostas_possiveis)
    
    return 'Desculpe, não entendi a pergunta.'

# Função principal do chatbot
def chatbot():
    print("Olá! Eu sou o ChatGPT. Como posso ajudar você hoje?")
    
    while True:
        pergunta = input("Você: ")
        
        if pergunta.lower() in saudacoes:
            print("ChatGPT: Olá!")
        elif pergunta.lower() in despedidas:
            print("ChatGPT: Adeus! Até mais.")
            break
        else:
            resposta = responder(pergunta)
            print(f"ChatGPT: {resposta}")

# Iniciar o chatbot
chatbot()
```

Este é apenas um exemplo simples de um chatbot que responde a algumas perguntas e cumprimentos. Você pode expandir o dicionário de respostas e adicionar lógica mais complexa para criar um chatbot mais inteligente e útil.

Lembre-se de que para criar um chatbot verdadeiramente inteligente, você pode precisar integrar serviços de Processamento de Linguagem Natural (NLP) e Aprendizado de Máquina, como o Dialogflow da Google, a API do GPT-3 da OpenAI ou outros recursos avançados de NLP.