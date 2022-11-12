import requests

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.4247129159058e-5,"date":"Sat, 12 Nov 2022 11:55:02 GMT","inverseRate":15564.897810831},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.2755552684365e-5,"date":"Sat, 12 Nov 2022 11:55:02 GMT","inverseRate":15934.844921685},"gbp":{"code":"GBP","alphaCode":"GBP","numericCode":"826","name":"U.K. Pound Sterling","rate":5.4879576820666e-5,"date":"Sat, 12 Nov 2022 11:55:02 GMT","inverseRate":18221.714851552}}

for data in json_data.values():
    print(data ['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
