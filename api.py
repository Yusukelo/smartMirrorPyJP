import requests
import feedparser


def getWeather(city: str):
    # plz,create openweathermap account and get your api_key
    api_key = ''
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ja&units=metric'

    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        json = r.json()
        return json
    else:
        print('error: status_code is {}'.format(r.status_code))
        return {}

def getNHKNews():
    url = 'https://www.nhk.or.jp/rss/news/cat0.xml'
    # local_url = f'https://www3.nhk.or.jp/lnews/{city}/toplist.xml '
    xml = feedparser.parse(url)
    if (xml) :
        news = xml.get("entries")
        length = len(news)
        return [news,length]
    else:
        return [None,0]

def getGPS():
    geo_url = 'https://get.geojs.io/v1/ip/geo.json'
    geo_request = requests.get(geo_url)
    if geo_request.status_code == requests.codes.ok:
        geo_data = geo_request.json()
        lat = geo_data.get("latitude")
        lon = geo_data.get("longitude")
        return [lat,lon]
    else:
        return ['35','139']






