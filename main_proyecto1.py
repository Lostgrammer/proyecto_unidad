#import pandas 
import pandas as pd
 



#opcion 1 mostrar libros guardados

def mostrar_libros_guardados():
    print("****************** ESTOS SON NUESTROS LIBROS GUARDADOS ******************")
    basedatoss = pd .read_csv(r'C:\Users\Fernando Leon\Desktop\ramaluis_2\csv\libros.csv')
    print(basedatoss)
    s = input("Presione cualquier tecla para volver al menú principal: ")
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
         
      
#funcion para ver los libros registrados

def ver_libros_reg():
    print('\n******************AQUÍ PUEDES VER LIBROS REGISTRADOS******************')
    for l in lista:
     print (l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)

     s = input("Presione cualquier tecla para volver al menú principal: ")
    print("")

    while s != 0:
        menu()
      
      
#fncion para poder registrar libros  

def registrarlibro():
    print("\nAQUI PUEDES REGISTRAR DATOS DE UN NUEVO LIBRO")
    print("*********************************************")
    l = libro()
    l.ids = (input("Introduzca el id del libro: "))
    l.título = (input("Introduzca el título del libro: "))
    l.género= (input("Introduzca a que género pertenece el libro: "))
    l.isbn= (input("Introduzca el ISBN del libro: "))
    l.editorial = (input("Introduzca la editorial del libro: "))
    l.autores = (input("Introduzca el autor o los autores del libro: "))
    lista.append(l)
    
    s = input("Presione cualquier tecla para volver al menú principal: ")
    print("")

    while s != 0:
        menu()
      
      
      
 #funcion para buscar libros por isbn o titulo
 
def buscarlibro():
    print("\n**********AQUÍ PUEDES BUSCAR DATOS DEL LIBRO POR ISBN O TÍTULO**********\n")
    filtro = input("ingrese isbn o titulo a buscar: ")

    for l in lista:
        if l.isbn == filtro or l.título == filtro:
            print("\n",l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)
    
    s = input("Presione cualquier tecla para volver al menú principal: ")
    print("")

    while s != 0:
        menu()













def menu() :
    selec = True
    print("BIENVENIDOS A LA MICROBIBLIOTECA")
    print("***************")
    while (selec==True):
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
        ingreso = (input("Su respuesta: "))
        if ingreso == '1':
            mostrar_libros_guardados()
            selec = True
        elif ingreso == '2':
            ver_libros_reg()
            selec = True
        elif ingreso == '3':
            registrarlibro()
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
            print('Programa finalizado. Hasta la próxima!!')
            selec = False
        else:
            print('\nAsigne un valor valido\n')
            input('Presione enter para continuar')
            selec = True

def main():
    menu()
if __name__ == '__main__':
    main()
