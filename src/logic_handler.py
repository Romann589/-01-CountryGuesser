import json
from country import Country

def load_countries_file(country_file):
    with open(country_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def load_countries(data):
    countries = []
    for country in data:
        cca3 = country['cca3']
        name_ger = country['translations']["deu"]["official"]
        capital = country['capital']
        borders = country['borders']
        population = country['population']
        continents = country['continents']
        
        # We extract them if they exist, or use placeholders
        flag_path = country.get('flag_path', "") 
        languages = country.get('languages', [])

        # FIX: Pass them in the exact order __init__ expects them
        countries.append(
            Country(
                country_name=name_ger,
                country_code=cca3,
                capital_city=capital,
                borders=borders,
                flag_path=flag_path,
                languages=languages, # Named to match your exact class init parameter
                population=population,
                continent=continents
            )
        )
    return countries
 