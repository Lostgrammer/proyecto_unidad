
import requests
import json

#Funcion para ver pokemones por generacion

peticion = requests.get ('https://pokeapi.co/api/v2/generation/')
datos = peticion.json()

def mostrar_generacion():
    ingreso_generacion = input("Ingrese generación para buscar sus respectivos pokemones (1 al 8): ")

    if ingreso_generacion == "1":
        lista_generacion = [datos_lista["0"]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "2":
        lista_generacion = [datos_lista[1]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "3":
        lista_generacion = [datos_lista[2]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "4":
        lista_generacion = [datos_lista[3]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "5":
        lista_generacion = [datos_lista[4]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "6":
        lista_generacion = [datos_lista[5]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "7":
        lista_generacion = [datos_lista[6]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    elif ingreso_generacion == "8":
        lista_generacion = [datos_lista[7]["name"] for datos_lista in datos["results"]]
        print(lista_generacion)

        lista_de_pokemones = [pokemon["name"] for pokemon in ["pokemon_species"]]
        print(lista_de_pokemones)

    else:
        print("\nAsigne un valor valido\n")
        input("Presione enter para continuar")





#funcion para ver pokemons por habitat

def mostrar_x_habitat(num):
    url = ("https://pokeapi.co/api/v2/pokemon-habitat/")
    peticion = requests.get(url + str(num) )
    datos = json.loads(peticion.content)
    s = [nombre['name'] for nombre in datos['pokemon_species']]
    print(s)


    print("**********AQUI PODRAS VER LOS POKEMONS QUE EXISTEN POR HABITAT**********")
    print("1 Pokémon de caverna.")
    print("2 Pokémon de bosque.")
    print("3 Pokémon de pradera.")
    print("4 Pokémon de montaña.")
    print("5 Pokémon de habitat desconocido.")
    print("6 Pokémon de terreno dificl.")
    print("7 Pokémon de mar.")
    print("8 Pokémon de ciudad.")
    print("8 Pokémon de agua.")
    num = int(input("\ningrese un numeor de acuerdo al habitat que desea ver: "))
    print("")
    mostrar_x_habitat(num)




#añadi funcion para ver pokemons por tipo
def mostrar_x_tipo(num):
    url = ("https://pokeapi.co/api/v2/type/")
    peticion = requests.get(url + str(num) )
    datos = json.loads(peticion.content)
    s = [pok['pokemon']['name'] for pok in datos['pokemon']]
    print(s)
    print("**********AQUI PODRAS VER LOS POKEMONS QUE EXISTEN POR Tipo**********")
    print("1 Pokémon de tipo normal.")
    print("2 Pokémon de tipo lucha.")
    print("3 Pokémon de tipo volador.")
    print("4 Pokémon de tipo veneno.")
    print("5 Pokémon de tipo tierra.")
    print("6 Pokémon de tipo roca.")
    print("7 Pokémon de tipo insecto.")
    print("8 Pokémon de tipo fantasma.")
    print("9 Pokémon de tipo acero.")
    print("10 Pokémon de tipo fuego.")
    print("11 Pokémon de tipo agua.")
    print("12 Pokémon de tipo planta.")
    print("13 Pokémon de tipo electrico.")
    print("14 Pokémon de tipo psiquico.")
    print("15 Pokémon de tipo hielo.")
    print("16 Pokémon de tipo dragon.")
    print("17 Pokémon de tipo oscuro.")
    print("18 Pokémon de tipo hada.")
    print("10001 Pokémon de tipo desconocido.")
    print("10002 Pokémon de tipo sombra.")

    num = int(input("\ningrese la el numero del tipo que quiere ver: "))
    print("")

    mostrar_x_tipo(num)

#mostrar habilidades
def mostrar_habilidades():
    peticion_habilidades = requests.get('https://pokeapi.co/api/v2/ability/')
    # manipular solo los datos que necesitamos
    habilidades = peticion_habilidades.json()
    lista_habilidad = habilidades["results"]
    tipos_habilidad = [tipo["name"] for tipo in habilidades["results"]]
    print(tipos_habilidad)


#Funcion de menu principal

def menu():
    selec = True
    print("BIENVENIDOS A NUESTRA POKEDEX XD")
    print("********************************")
    while selec == True:
        print("--Elija una de las opciones:--")
        print("1. VER POKEMONS POR GENERACION")
        print("2. VER POKEMONS POR FORMA")
        print("3. VER POKEMON POR HABILIDADES")
        print("4. VER POKEMONS POR HABITATS.")
        print("5. VE RPOKEMONS POR TIPOS.")

        ingreso = input("Su respuesta: ")
        if ingreso == "1":
            mostrar_generacion()
            selec = True
        elif ingreso == "2":
            mostrar_forma()
            selec = True
        elif ingreso == "3":
            mostrar_habilidades()
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

