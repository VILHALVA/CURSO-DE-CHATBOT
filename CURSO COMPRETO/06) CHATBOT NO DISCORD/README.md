# CHATBOT NO DISCORD
Para criar um chatbot no Discord, você pode usar a biblioteca `discord.py`, que é uma API Python para interagir com a plataforma Discord. O Discord é uma plataforma de comunicação amplamente utilizada por jogadores e comunidades online, e a criação de um bot para Discord pode adicionar funcionalidades personalizadas a servidores do Discord. Aqui está um exemplo de como criar um bot simples usando `discord.py`:

**Passo 1: Configurar um Bot no Discord Developer Portal**

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications).
2. Clique em "New Application" para criar uma nova aplicação. Dê um nome à sua aplicação (isso será o nome do seu bot).
3. No painel esquerdo, vá para "Bot" e clique em "Add Bot". Isso criará um bot associado à sua aplicação.
4. Na seção "Token", clique em "Copy" para copiar o token de autenticação do bot. Você precisará deste token no código Python.

**Passo 2: Escrever o Código Python para o Bot**

Você deve instalar a biblioteca `discord.py` antes de começar:

```bash
pip install discord.py
```

Aqui está um exemplo simples de código Python para criar um bot que responde a comandos no Discord:

```python
import discord
from discord.ext import commands

# Defina o prefixo dos comandos (por exemplo, !bot)
bot = commands.Bot(command_prefix='!')

# Evento para exibir uma mensagem quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f'Bot está pronto: {bot.user.name}')

# Comando simples para cumprimentar o bot
@bot.command()
async def oi(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

# Conecte o bot ao servidor usando o token
bot.run('SEU_TOKEN_DO_BOT')
```

**Passo 3: Adicionar o Bot a um Servidor do Discord**

1. No portal de desenvolvedor do Discord, vá para a seção "OAuth2".
2. Em "OAuth2 URL Generator", marque a opção "bot" e escolha as permissões necessárias para o seu bot.
3. Copie o URL gerado e cole-o em um navegador para adicionar o bot a um servidor do Discord.

**Passo 4: Executar o Bot**

Execute o código Python que você escreveu para iniciar o bot. Ele deve responder a comandos no servidor do Discord.

Observe que este é apenas um exemplo simples de um bot no Discord. Você pode personalizá-lo e adicionar mais funcionalidades, como responder a comandos personalizados, interagir com APIs externas ou realizar tarefas específicas para o seu servidor do Discord. Certifique-se de consultar a documentação do `discord.py` para explorar recursos adicionais e funcionalidades avançadas.