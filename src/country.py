class Country:
    def __init__(
        self, 
        country_name: str, 
        country_code: str, 
        capital_city: list, 
        borders: list, 
        flag_path: str,
        languages: list,   
        population: int, 
        continent: str
    ):
        self.country_name = country_name
        self.country_code = country_code
        self.capital_city = capital_city
        self.borders = borders
        self.flag_path = flag_path
        self.languages = languages
        self.population = population
        self.continent = continent