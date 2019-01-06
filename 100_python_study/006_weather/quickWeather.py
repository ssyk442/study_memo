import sys
import urllib.request
import urllib.parse
import json

# コマンドライン引数から地域名を組み立てる
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = ' '.join(sys.argv[1:])

# OpenWeatherMap.orgのAPIから取得したAPIキーを定義しておく
APPID = input("input appid: ")

# パラメータをURLエンコードする
values = {
    'q': location,
    'appid': APPID
}
params = urllib.parse.urlencode(values)

# OpenWeatherMap.orgのAPIからJSONデータをダウンロードする
url = "http://api.openweathermap.org/data/2.5/weather?" + params
print("url=", url)

# JSONデータからPython変数に読み込む
data = urllib.request.urlopen(url).read()
print(data)
