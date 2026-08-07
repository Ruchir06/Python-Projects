import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url= f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print(f"failed to retrieve data {response.status_code}")

pokmeon_name = "pikachu"

get_pokemon_info(pokmeon_name)