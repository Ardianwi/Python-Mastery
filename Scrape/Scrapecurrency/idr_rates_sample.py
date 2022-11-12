import requests


#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.4247129159058e-5,"date":"Fri, 11 Nov 2022 23:55:02 GMT","inverseRate":15564.897810831}}



for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])



