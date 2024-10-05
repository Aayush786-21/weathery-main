import requests

def get_weather(city):
    api_key = 'ee3ec7d5241b100b41e0f0bc043218d9' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return weather_description, temperature
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None
