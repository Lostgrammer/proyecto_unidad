# import pandas
import pandas as pd

# opcion 1 leer libros guardados
def leer_libros():

    basedatoss = pd.read_csv(
        "Libros.csv"
    )
    print('Libros cargados correctamente')
    s = input("Presione cualquier tecla para volver al menú principal: \n")

# opcion 2 mostrar libros guardados
def mostrar_libros_guardados():
    print("****************** ESTOS SON NUESTROS LIBROS GUARDADOS ******************")
    basedatoss = pd.read_csv(
        "Libros.csv"
    )
    print(basedatoss.to_string())
    s = input("Presione cualquier tecla para volver al menú principal: \n")

# define clase
global lista
lista = list()

class libro:
    def __init__(self):
        self.ids = ""
        self.título = ""
        self.género = ""
        self.isbn = ""
        self.editorial = ""
        self.autores = ""

# funcion para ver los libros registrados
def ver_libros_reg():
    print("\n******************AQUÍ PUEDES VER LIBROS REGISTRADOS******************")
    for l in lista:
        print(
            l.ids,
            "-",
            l.título,
            "-",
            l.género,
            "-",
            l.isbn,
            "-",
            l.editorial,
            "-",
            l.autores,
        )

        s = input("Presione cualquier tecla para volver al menú principal: \n")

# opcion 3 funcion para poder registrar libros
def registrarlibro():
    print("\nAQUI PUEDES REGISTRAR DATOS DE UN NUEVO LIBRO")
    print("*********************************************")
    l = libro()
    l.ids = input("Introduzca el id del libro: ")
    l.título = input("Introduzca el título del libro: ")
    l.género = input("Introduzca a que género pertenece el libro: ")
    l.isbn = input("Introduzca el ISBN del libro: ")
    l.editorial = input("Introduzca la editorial del libro: ")
    l.autores = input("Introduzca el autor o los autores del libro: ")
    lista.append(l)
    s = input("Presione cualquier tecla para volver al menú principal: \n")

# opcion 5 funcion para buscar libros por isbn o titulo
def buscarlibro():
    print(
        "\n**********AQUÍ PUEDES BUSCAR DATOS DEL LIBRO POR ISBN O TÍTULO**********\n"
    )
    filtro = input("ingrese isbn o titulo a buscar: ")

    for l in lista:
        if l.isbn == filtro or l.título == filtro:
            print(
                "\n",
                l.ids,
                "-",
                l.título,
                "-",
                l.género,
                "-",
                l.isbn,
                "-",
                l.editorial,
                "-",
                l.autores,
            )

    s = input("Presione cualquier tecla para volver al menú principal: \n")

# opcion 6 funcion ordenar por titulos


#opcion 7 funcion buscar libro por autor
def buscar_libro():
    basedatoss = pd.read_csv(
        "Libros.csv"
    )
    s=True
    while(s==True):
        ingreso=input('\n Por cual tipo desea buscar? Autor / Editorial / Genero \n').upper()
        if(ingreso=='AUTOR'):
            print(basedatoss['autor'])
            lista = []
            entrada = input('Que autor quiere buscar?\n').lower()
            #el .apply es para modificar los valores a minusculas y asi pueda compararse con el input
            for i in basedatoss['autor'].apply(str.lower):
                if (entrada in i):
                    lista.append(i)
            print(lista)
            s=False
        elif(ingreso=='EDITORIAL'):
            print(basedatoss['editorial'])
            lista = []
            entrada = input('Que editorial quiere buscar?\n').lower()
            for i in basedatoss['editorial'].apply(str.lower):
                if (entrada in i):
                    lista.append(i)
            print(lista)
            s=False
        elif (ingreso == 'GENERO'):
            print(basedatoss['genero'])
            lista = []
            entrada = input('Que genero quiere buscar?\n').lower()
            for i in basedatoss['genero'].apply(str.lower):
                if (entrada in i):
                    lista.append(i)
            print(lista)
            s = False
        else:
            print('Asigne un valor valido')
            s=True
    input('Presione enter para continuar\n')

def menu():
    selec = True
    print("BIENVENIDOS A LA MICROBIBLIOTECA")
    print("***************")
    while selec == True:
        print("--Elija una de las opciones:--")
        print("1. Cargar libros guardados")
        print("2. Mostrar libros")
        print("3. Agregar información de un nuevo libro")
        print("4. Eliminar un libro")
        print("5. Buscar libro por codigo ISBN")
        print("6. Ordenar libros por titulo")
        print("7. Buscar libro por autor, editorial, género")
        print("8. Buscar libro por cantidad de autores")
        print("9. Editar datos de un libro")
        print("10. Guardar libro")
        print("11. Terminar.")
        ingreso = input("Su respuesta: ")
        if ingreso == "1":
            leer_libros()
            selec = True
        elif ingreso == "2":
            mostrar_libros_guardados()
            selec = True
        elif ingreso == "3":
            registrarlibro()
            selec = True
        elif ingreso == "4":
            eliminarlibro()
            selec = True
        elif ingreso == "5":
            buscarlibro()
            selec = True
        elif ingreso == "6":
            libro.buscar_titulo()
            selec = True
        elif ingreso == "7":
            print(buscar_libro())
            selec = True
        elif ingreso == "8":
            print("ga")
            selec = True
        elif ingreso == "9":
            print("ga")
            selec = True
        elif ingreso == "10":
            print("ga")
            selec = True
        elif ingreso == "11":
            print("Programa finalizado. Hasta la próxima!!")
            selec = False
        else:
            print("\nAsigne un valor valido\n")
            input("Presione enter para continuar")
            selec = True

def main():
    menu()

if __name__ == "__main__":
    main()
