#! /usr/bin/python2.7
import requests
def get_weather_forecast():

    #Connecting to the Weather API
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Miami&units=imperial&appid=aff57df94aca6994be2dc6dcbc0820cd'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    #Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    #Creating forecast String
    forecast = 'The forecast for Miami today is '
    forecast += description + ' with a high of ' + str(temp_max)
    forecast += ' and a low of ' + str(temp_min) + '.'

    return forecast
