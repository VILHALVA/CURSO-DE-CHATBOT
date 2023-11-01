import tweepy

# Chaves e tokens de acesso obtidos no passo 1
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SEU_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Configure a autenticação com o Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crie uma instância da API do Twitter
api = tweepy.API(auth)

# Função para responder a menções
def responder_mencao():
    mentions = api.mentions_timeline()

    for mention in mentions:
        tweet_id = mention.id
        username = mention.user.screen_name
        mensagem = f'Olá, @{username}! Obrigado por mencionar-me.'
        
        # Responda à menção
        api.update_status(status=mensagem, in_reply_to_status_id=tweet_id)

# Execute a função para responder a menções
responder_mencao()
