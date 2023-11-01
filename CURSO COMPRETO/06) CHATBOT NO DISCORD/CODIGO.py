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
