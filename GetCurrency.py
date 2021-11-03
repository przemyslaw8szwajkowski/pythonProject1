import math
from datetime import date

import requests
import json


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# przeliczony kurs kupna waluty
def GetCurrencyTodayRatesBid(code):
    # code.upper()
    r = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/c/{code}/today/?format=json")
    y = json.loads(r.content)
    bid = y["rates"][0]['bid']
    return round_up(bid, 2)

#przeliczony kurs sprzedaży waluty
def GetCurrencyTodayRatesAsk(code):
    # code.upper()
    r = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/c/{code}/today/?format=json")
    y = json.loads(r.content)
    ask = y["rates"][0]['ask']
    return round_up(ask, 2)

print(f"Wartość Waluty z dnia: {date.today()}")
print(f"Kupno EURO: {GetCurrencyTodayRatesBid('EUR')} zł")
print(f"Sprzedaż EURO: {GetCurrencyTodayRatesAsk('EUR')} zł")

print(f"Kupno DOLAR: {GetCurrencyTodayRatesBid('USD')} zł")
print(f"Sprzedaż DOLAR: {GetCurrencyTodayRatesAsk('USD')} zł")

print(f"Kupno FRANK SZWAJCARSKI: {GetCurrencyTodayRatesBid('CHF')} zł")
print(f"Sprzedaż FRANK SZWAJCARSKI: {GetCurrencyTodayRatesAsk('CHF')} zł")



