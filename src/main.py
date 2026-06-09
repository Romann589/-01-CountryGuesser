import flet as ft
from flet import View, Text, Row, View, Page, AppBar, ElevatedButton, Text, IconButton, Image
from countries_loader import load_countries_file, load_countries

def init_game():
    countries_json = load_countries_file("countries.json")
    countries = load_countries(countries_json)
    return countries

def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    countries_loaded = init_game()
    print(countries_loaded[0].country_name)

    def start_game(e):
        print("Game started")

    page.views.append(View(route="/", controls=[
        Text(value="Country Guess", size=30),
        Text(value="Population Guess", size=30),
        ElevatedButton(text="Continent Guess", on_click=start_game),]))

    page.update()
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
 