import json
import requests

def get_weather_forecast():
    # Obter a previsão do tempo para a cidade atual
    url = "https://api.openweathermap.org/data/2.5/weather?q=sao-paulo,br&appid=YOUR_API_KEY"
    response = requests.get(url)
    weather_data = json.loads(response.content)

    # Extrair as informações do clima
    weather_description = weather_data["weather"][0]["description"]
    weather_temperature = weather_data["main"]["temp"]

    # Retornar as informações do clima
    return weather_description, weather_temperature

def main():
    # Obter as informações do clima
    weather_description, weather_temperature = get_weather_forecast()

    # Enviar as informações do clima para o usuário
    print("O clima hoje é de", weather_description, "com temperatura média de", weather_temperature)

if __name__ == "__main__":
    main()
