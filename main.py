import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c0fddb02d9e43aca21f7452c210f31ff'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_pokemon = {
    "name": "Bulba",
    "photo_id": 5
}

body_rename = {
    "pokemon_id": "349597",
    "name": "Uffff",
    "photo_id": 5
}

body_add = {
     "pokemon_id": "349597"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)