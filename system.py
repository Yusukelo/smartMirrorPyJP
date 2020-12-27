import datetime
import time
from PIL import Image, ImageTk

import api

settings = dict(
    # True: 12hour round, False: 24hour round
    AMPM=False,
    # en:English, ja:Japanese
    lang='ja',
    # To find your city available,search by here.
    #https://openweathermap.org/find
    location='Yokohama, JP'
)
def nowTime():
    AMPM = settings.get("AMPM")
    dt_now = datetime.datetime.now()
    if (AMPM):
        if dt_now.hour < 12:
            s = 'AM{0:02d}:{1:02d}:{2:02d}'.format(dt_now.hour, dt_now.minute, dt_now.second)
        else:
            nowhour = dt_now.hour - 12
            s = 'PM{0:02d}:{1:02d}:{2:02d}'.format(nowhour, dt_now.minute, dt_now.second)
    else:
        s = '{0:02d}:{1:02d}:{2:02d}'.format(
            dt_now.hour, dt_now.minute, dt_now.second)
    return s
def nowDate():
    date = datetime.datetime.now()
    weekday = date.weekday()
    dict_week = {0:'月', 1:'火', 2:'水', 3:'木', 4:'金', 5:'土', 6:'日'}
    weekJP = dict_week.get(weekday)
    w = '{0}曜日'.format(weekJP)

    s = '{0}月{1}日'.format(date.month, date.day)
    return [s,w]
def weatherJP(weatherEn):
    dict_weather = {'Sun':'晴れ','Clouds':'曇り','Rain':'雨','Snow':'雪','Thunder':'雷'}
    weatherJP = dict_weather.get(weatherEn)
    if (weatherJP):
        return weatherJP
    else:
        return weatherEn

def getWeather():
    location = settings.get("location")
    lang = settings.get("lang")
    data = api.getWeather(location)
    weather_main = data.get('weather')[0].get('main')
    if lang == 'ja':
        weather_main = weatherJP(weather_main)

    temp = f'{data.get("main").get("temp")}°'
    location = data.get('sys').get('name')
    icon_file = data.get('weather')[0].get('icon')
    icon_file = icon_file[:2]
    if icon_file == '04':
        icon_file = '03'
    if icon_file == '10':
        icon_file = '09'
    image = Image.open(f"assets/{icon_file}.png")
    print(image)
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = image.convert('RGB')
    photo = ImageTk.PhotoImage(image)

    return [weather_main,temp,photo,location]
