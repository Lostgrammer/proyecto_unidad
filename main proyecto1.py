import pandas as pd
#para inporta archivo csv 
basedatoss = pd .read_csv(r'C:\Users\Fernando Leon\Desktop\ramaluis_2\csv\libros.csv')


#opcion 1 mostrar libros guardados
def mostrar_libros_guardados():
            print("********** ESTOS SON NUESTROS LIBROS GUARDADOS **********")
            print(basedatoss)

            s = int(input("presione 0 para volver al menú principal: "))
            print("")

            while s != 0:
             menu()
            
#define clase
global lista
lista = list()
class libro:
    def __init__(self):
     self.ids = ""
     self.título = ""
     self.género = ""
     self.isbn = ""
     self.editorial =""
     self.autores = ""
            
         
#fncion para poder registrar libros    
def registrarlibro():
    print("\nAQUI PUEDES REGISTRAR DATOS DE UN NUEVO LIBRO")
    print("*********************************************")
    l = libro()
    l.ids = (input("introduzca el id del libro: "))
    l.título = (input("introduzca el título del libro: "))
    l.género= (input("introduzca a que género pertenece el libro: "))
    l.isbn= (input("introduzca el isbn del libro: "))
    l.editorial = (input("introduzca la editorial del libro: "))
    l.autores = (input("introduzca el el autor o los autores del libro: "))
    lista.append(l)
    s = int(input("\npresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()
#funcion para ver los libros registrados
def ver_libros_reg():
    print('\n**********AQUI PUEDES VER LIBROS REGISTRADOS**********')
    for l in lista:
        print (l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)

    s = int(input("\npresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()

#funcion para buscar libros por isbn o titulo
def buscarlibro():
    print("\n**********AQUI PUEDES BUSCAR DATOS DEL LIBRO POR ISBN O TÍTULO**********\n")
    filtro = input("ingrese isbn o titulo a buscar: ")

    for l in lista:
        if l.isbn == filtro or l.título == filtro:
            print("\n",l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)
    
    s = int(input("\npresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()
