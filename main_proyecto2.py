'''url_generacion = 'https://pokeapi.co/api/v2/generation/'
url_forma_pokemon = 'https://pokeapi.co/api/v2/pokemon-form/'
url_habilidades = 'https://pokeapi.co/api/v2/ability/'
url_habitad = 'https://pokeapi.co/api/v2/pokemon-habitat/'
url_tipos = 'https://pokeapi.co/api/v2/type/''''


import requests

if __name__ == '__main__':
    url_generacion = 'https://pokeapi.co/api/v2/generation'

    respuesta = requests.get(url_generacion)
    if respuesta.status_code == 200:

        payload = respuesta.json()
        resultados = payload.get('resultados', [])

        if resultados:
            for generacion in resultados:
                numero = generacion['numero']
                print("Las generaciones son :", numero)