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
def menu() :
    selec = 0
    salir = 10
    print("\nBIENVENIDOS A LA MICROBIBLIOTECA")
    print("********************************")
    while selec != salir:
        print("\n--Elija una de las opciones:--\n")
        print("1. Mostrar libros guardados")
        print("2. Agregar información de un nuevo libro")
        print("3. Ver libros registrados")
        print("4. Eliminar un libro")
        print("5. Buscar libro por código ISBN")
        print("6. Ordenar libros por título")
        print("7. Buscar libro por autor, editorial, género")
        print("8. Buscar libro por cantidad de autores")
        print("9. Editar datos de un libro")
        print("10. Guardar libro")
        selec = int(input("Ingrese su opción: "))

        if selec == 1:
            mostrar_libros_guardados()
        elif selec == 2:
            registrarlibro()
        elif selec == 3:
            ver_libros_reg()
        elif selec == 4:
            eliminarlibro()
        elif selec == 5:
            buscarlibro()
        elif selec == 6:
            print('ga')
        elif selec == 7:
            print('ga')
        elif selec == 8:
            buscarlibro()
        elif selec == 9:
            print('ga')
        elif selec == 10:
            print('ga')
        else:
            print('Asigne un valor valido')              
menu()
