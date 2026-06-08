import json
import requests

url = "https://restcountries.com/v3.1/all?fields=cca3,flags,borders,capital,continents,translations,languages,population"
response = requests.get(url)
if response.status_code == 200:
    countries = response.json()
with open("countries.json", "w", encoding="utf-8") as file:
    json.dump(countries, file, indent=4, ensure_ascii=False)