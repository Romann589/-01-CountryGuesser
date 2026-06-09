import json

def load_country_file(country_file):
    with open(country_file) as f:
        country_dict = json.load(f)
    return country_dict
def load_countries(country_dict):
    countries = []
    for country in country_dict:
        print(country)