import requests, json

APIKey = '338ebfa074a6c17c9d1872b45230e82c'

def GetTemp(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}"
    output = requests.get(URL).json()
    temperature = float(output['main']['temp'])
    #countryISO = (output['sys']['country'])
    return f'{(temperature - 273.15):.2f}'
