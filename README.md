# smartMirrorPyJP
日本版スマートミラープロジェクトです。

##　機能

・時計
時間を表示します。

・天気
現在地の今の天気、気温を表示します。

## 使用方法

1. git clone にてこのリポジトリをダウンロード

```
git clone https://github.com/Yusukelo/smartMirrorPyJP/
```

2.Tkinterのインストール

Macの場合インストールが必要な様です。

3. パッケージをインストール
requirements.txtにある通りのパッケージをインストールしてください。

pipを使用している場合、以下のコマンドでインストール出来ます。

```
pip install -r requirements.txt 
```

4.[OpenWeather](https://openweathermap.org/)にてアカウントを作成し,api_keyを取得。
smartMirrorPyJP/api.pyにapiKeyを配置。
smartMirrowPyJP/api.py
```
def getWeather(city: str):
    # plz,create openweathermap account and get your api_key
    api_key = ''　←here!!
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ja&units=metric'
```

5.
smartMirrorPyJP/system.pyでsettingを記入。

smartMirrorPyJP/system.py
```
settings = dict(
    # True: 12hour round, False: 24hour round
    AMPM=False,
    # en:English, ja:Japanese
    lang='ja',
    # To find your city available,search by here.
    #https://openweathermap.org/find
    location='Yokohama, JP'
)
```
6. Run!!

## ライセンス
MIT.



