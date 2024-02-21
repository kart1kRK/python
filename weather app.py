import requests 
import json
import os

city=input("Enter your city name\n")

url = f"https://api.weatherapi.com/v1/current.json?key=3ad74c8470394751be462642241902&q={city}"

r= requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degrees '")