class Country:

    def __init__(self, country_name: str, country_code: str,
                 capital_city: str, borders: list, population: int, continents: list):
        self.country_name = country_name
        self.country_code = country_code
        self.capital_city = capital_city
        self.borders = borders
        self.population = population
        self.continents = continents
