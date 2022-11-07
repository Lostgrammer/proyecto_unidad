import requests
import json
"""
url_generacion = 'https://pokeapi.co/api/v2/generation/'
url_forma_pokemon = 'https://pokeapi.co/api/v2/pokemon-form/'
url_habilidades = 'https://pokeapi.co/api/v2/ability/'
url_habitad = 'https://pokeapi.co/api/v2/pokemon-habitat/'
url_tipos = 'https://pokeapi.co/api/v2/type/
'"""


def menu():
    selec = True
    print("BIENVENIDOS A NUESTRA POKEDEX XD")
    print("********************************")
    while selec == True:
        print("--Elija una de las opciones:--")
        print("1. VER POKEMONS POR GENERACIÓN")
        print("2. VER POKEMONS POR FORMA")
        print("3. VER POKEMON POR HABILIDADES")
        print("4. VER POKEMONS POR HABITATS.")
        print("5. VER POKEMONS POR TIPOS.")
        
        ingreso = input("Su respuesta: ")
        if ingreso == "1":
            ga()
            selec = True
        elif ingreso == "2":
            ga()
            selec = True
        elif ingreso == "3":
            ga()
            selec = True
        elif ingreso == "4":

            mostrar_x_habitat(num)
            
            selec = True
        elif ingreso == "5":

            mostrar_x_tipo(num)
            
            selec = True
        else:
            print("\nAsigne un valor valido\n")
            input("Presione enter para continuar")
            selec = True

def main():
    menu()

if __name__ == "__main__":
    main()

