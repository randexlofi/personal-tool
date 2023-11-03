import requests, json

APIKey = 'YOUR_API_KEY'

def GetTemp(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}"
    output = requests.get(URL).json()
    temperature = float(output['main']['temp'])
    #countryISO = (output['sys']['country'])
    return f'{(temperature - 273.15):.2f}'
