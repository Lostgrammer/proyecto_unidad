import requests
import json


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