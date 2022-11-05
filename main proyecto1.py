import pandas as pd
#para inporta archivo csv 
basedatoss = pd .read_csv(r'C:\Users\Fernando Leon\Desktop\ramaluis_2\csv\libros.csv')


#opcion 1 mostrar libros guardados
def mostrar_libros_guardados():
            print("********** ESTOS SON NUESTROS LIBROS GUARDADOS **********")
            print(basedatoss)

            s = int(input("Presione 0 para volver al menú principal: "))
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
    print("\nAQUÍ PUEDES REGISTRAR DATOS DE UN NUEVO LIBRO")
    print("*********************************************")
    l = libro()
    l.ids = (input("Introduzca el id del libro: "))
    l.título = (input("Introduzca el título del libro: "))
    l.género= (input("Introduzca a que género pertenece el libro: "))
    l.isbn= (input("Introduzca el ISBN del libro: "))
    l.editorial = (input("Introduzca la editorial del libro: "))
    l.autores = (input("Introduzca el autor o los autores del libro: "))
    lista.append(l)
    s = int(input("\nPresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()


#funcion para ver los libros registrados
def ver_libros_reg():
    print('\n**********AQUI PUEDES VER LIBROS REGISTRADOS**********')
    for l in lista:
        print (l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)

    s = int(input("\nPresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()


#funcion para buscar libros por isbn o titulo
def buscarlibro():
    print("\n**********AQUI PUEDES BUSCAR DATOS DEL LIBRO POR ISBN O TÍTULO**********\n")
    filtro = input("Ingrese ISBN o título a buscar: ")

    for l in lista:
        if l.isbn == filtro or l.título == filtro:
            print("\n",l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)
    
    s = int(input("\nPresione 0 para volver al menú principal: "))
    print("")

    while s != 0:
        menu()




#funcion menu
"""def menu() :
    selec = 0
    salir = 10"""
def menu() :
    selec = True
    print("BIENVENIDOS A LA MICROBIBLIOTECA")
    print("***************")
    while (selec==True):
        print("--Elija una de las opciones:--")
        print("1. Cargar libros guardados")
        print("3. Agregar informacion de un nuevo libro")
        print("2. Mostrar libros")
        print("4. Eliminar un libro")
        print("5. Buscar libro por codigo ISBN")
        print("6. Ordenar libros por titulo")
        print("7. Buscar libro por autor, editorial, genero")
        print("8. Buscar libro por cantidad de autores")
        print("9. Editar datos de un libro")
        print("10. Guardar libro")
        print("11. Terminar.")
        ingreso = (input("Su respuesta: "))
        if ingreso == '1':
             mostrar_libros_guardados()
            selec = True
        elif ingreso == '2':
            registrarlibro())
            selec = True
        elif ingreso == '3':
            er_libros_reg()
            selec = True
        elif ingreso == '4':
             eliminarlibro()
            selec = True
        elif ingreso == '5':
            buscarlibro()
            selec = True
        elif ingreso == '6':
            libro.buscar_titulo()
            selec = True
        elif ingreso == '7':
            print(libro.buscar_libro())
            selec = True
        elif ingreso == '8':
            print('ga')
            selec = True
        elif ingreso == '9':
            print('ga')
            selec = True
        elif ingreso == '10':
            print('ga')
            selec = True
        elif ingreso =='11':
            print('Programa finalizado. Hasta la proxima!!')
            selec = False
        else:
            print('\nAsigne un valor valido\n')
            input('Presione enter para continuar')
            selec = True
