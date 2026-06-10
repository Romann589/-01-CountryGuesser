import flet as ft
from flet import CupertinoNavigationBar, View, Text, Row, Page, AppBar, Button, IconButton, Image, FloatingActionButton, SafeArea, Container
from logic_handler import load_countries_file, load_countries
from country import Country
import random

def init_game():
    countries_json = load_countries_file("countries.json")
    countries = load_countries(countries_json)
    return countries

def get_random_country(countries_loaded: list[Country]):
    # Prevent crashing if we run out of countries!
    if len(countries_loaded) == 0:
        return None 
    random__int = random.randrange(len(countries_loaded))
    return countries_loaded.pop(random__int)

def main(page: ft.Page):
    page.title = "Country Guesser"
    countries_loaded: list[Country] = init_game()
    
    # 1. Grab our very first random country to start the app
    current_country = get_random_country(countries_loaded)
    
    def route_change(e):
        page.update()
        
    page.on_route_change = route_change

    # 2. Define our UI components as variables so we can update them later!
    flag_image = Image(
        src=f"{current_country.country_code}.png", 
        width=600, 
        height=200, 
        repeat=ft.ImageRepeat.NO_REPEAT
    )
    name_text = ft.Text(value=f'Name: {current_country.country_name}', size=30)
    code_text = ft.Text(value=current_country.country_code, size=30)
    capital_text = ft.Text(value=str(current_country.capital_city), size=30)
    pop_text = ft.Text(value=str(current_country.population), size=30)
    continent_text = ft.Text(value=str(current_country.continent), size=30)

    # 3. The actual Game Loop function!
    def guess_country(e):
        new_country = get_random_country(countries_loaded)
        
        if new_country:
            # Overwrite the UI variables with the new country's data
            flag_image.src = f"{new_country.country_code}.png"
            name_text.value = f'Name: {new_country.country_name}'
            code_text.value = new_country.country_code
            capital_text.value = str(new_country.capital_city)
            pop_text.value = str(new_country.population)
            continent_text.value = str(new_country.continent)
            
            # Tell Flet to redraw the screen with the new data
            page.update()
        else:
            name_text.value = "You guessed them all!"
            page.update()
            print("Game Over! No more countries.")
    
    nav_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.TEAL_400,
        inactive_color=ft.Colors.WHITE,
        active_color=ft.Colors.BLACK,
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE_OUTLINED, selected_icon=ft.Icons.EXPLORE, label="ATLAS"),
            ft.NavigationBarDestination(icon=ft.Icons.GAMEPAD_OUTLINED, selected_icon=ft.Icons.GAMEPAD, label="PLAY"),
            ft.NavigationBarDestination(icon=ft.Icons.BAR_CHART_OUTLINED, selected_icon=ft.Icons.BAR_CHART, label="STATS"),
        ],
    )

    page.views.append(
        View(
            route="/",
            navigation_bar=nav_bar,
            controls=[
                # 4. Drop our variables into the controls list
                flag_image,
                name_text,
                code_text,
                capital_text,
                pop_text,
                continent_text,
                
                ft.Button(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.ALARM),
                            ft.Text(value="Next Country"), # Changed text to fit the new function
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    on_click=guess_country, # Wire the button to our new function
                ),
            ]
        )
    )
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")