import json
import requests

def get_channel_info(channel_id):
    # Obter informações do canal
    url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id=" + channel_id
    response = requests.get(url, headers={"Authorization": "Bearer YOUR_API_KEY"})
    channel_data = json.loads(response.content)

    # Extrair as informações do canal
    channel_name = channel_data["items"][0]["snippet"]["title"]
    channel_subscribers = channel_data["items"][0]["statistics"]["subscriberCount"]
    channel_videos = channel_data["items"][0]["statistics"]["videoCount"]

    # Retornar as informações do canal
    return channel_name, channel_subscribers, channel_videos

def main():
    # Obter as informações do canal
    channel_name, channel_subscribers, channel_videos = get_channel_info("YOUR_CHANNEL_ID")

    # Enviar as informações do canal para o usuário
    print("O nome do canal é", channel_name)
    print("O canal tem", channel_subscribers, "inscritos")
    print("O canal tem", channel_videos, "vídeos")
