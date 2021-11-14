import requests


def get_prediction(city_name):
    APIkey = '1661b675f7716f259079b16051d428d0'
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={APIkey}')
    if r.json()['cod'] == '404':
        print('error 404 prediction.py')
    else:
        take_temp = r.json()['main']
        temp = round((take_temp['temp'] - 273.15), 1)
        temp_max = round((take_temp['temp_max'] - 273.15), 1)
        temp_min = round((take_temp['temp_min'] - 273.15), 1)
        # print(round((info["temp"] - 273.15), 1), '℃')
        return temp_min, temp, temp_max