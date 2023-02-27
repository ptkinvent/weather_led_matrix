import os
import requests
import json

class WeatherClient():
    def __init__(self, latitude, longitude):
        api_key = os.environ.get('PRIVATE_API_KEY')
        forecast_num_days = 7

        self.current_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}'
        self.forecast_url = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={latitude}&lon={longitude}&units=imperial&cnt={forecast_num_days}&appid={api_key}'
        self.air_pollution_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}'

        self.data = {}

    def query_weather(self):
        try:
            current_response = requests.get(self.current_url)
            print('\nReceived current response:', current_response.text)
            current_data = json.loads(current_response.text)

            self.data['curr_temp'] = current_data['main']['temp'] # Deg F
            self.data['description'] = current_data['weather'][0]['description']
            self.data['sunrise_time'] = current_data['sys']['sunrise'] # Datetime
            self.data['sunset_time'] = current_data['sys']['sunset'] # Datetime
            self.data['feels_like_temperature'] = current_data['main']['feels_like'] # Deg F
            self.data['pressure'] = current_data['main']['pressure'] # Pa
            self.data['humidity'] = current_data['main']['humidity'] # %
            self.data['wind_speed'] = current_data['wind']['speed'] # mph
        except:
            print('Failed to get current weather response')

        try:
            forecast_response = requests.get(self.forecast_url)
            print('\nReceived forecast response:', forecast_response.text)
            forecast_data = json.loads(forecast_response.text)

            self.data['high_temp'] = forecast_data['list'][0]['temp']['max'] # Deg F
            self.data['low_temp'] = forecast_data['list'][0]['temp']['min'] # Deg F
        except:
            print('Failed to get forecast weather response')

        try:
            air_pollution_response = requests.get(self.air_pollution_url)
            print('\nReceived air pollution response:', air_pollution_response.text)
            air_pollution_data = json.loads(air_pollution_response.text)

            self.data['aqi'] = air_pollution_data['list'][0]['main']['aqi'] # '1'-'5'
        except:
            print('Failed to get air pollution. response')
