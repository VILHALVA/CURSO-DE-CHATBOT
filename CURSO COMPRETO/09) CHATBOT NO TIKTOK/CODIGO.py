import json
import requests

def get_video_info(video_id):
    # Obter informações do vídeo
    url = "https://www.tiktok.com/api/v1/videos/" + video_id
    response = requests.get(url, headers={"Authorization": "Bearer YOUR_API_KEY"})
    video_data = json.loads(response.content)

    # Extrair as informações do vídeo
    video_title = video_data["item"]["title"]
    video_views = video_data["item"]["statistics"]["viewCount"]
    video_published_at = video_data["item"]["publishedAt"]

    # Retornar as informações do vídeo
    return video_title, video_views, video_published_at

def main():
    # Obter as informações do vídeo
    video_title, video_views, video_published_at = get_video_info("YOUR_VIDEO_ID")

    # Enviar as informações do vídeo para o usuário
    print("O título do vídeo é", video_title)
    print("O vídeo tem", video_views, "visualizações")
    print("O vídeo foi publicado em", video_published_at)
