#import pandas 
import pandas as pd
 



#opcion 1 mostrar libros guardados

def mostrar_libros_guardados():
    print("****************** ESTOS SON NUESTROS LIBROS GUARDADOS ******************")
    basedatoss = pd .read_csv(r'C:\Users\Fernando Leon\Desktop\ramaluis_2\csv\libros.csv')
     print(basedatoss)
       s = input("presione cualquier tecla para volver al menú principal: ")
            print("")

            while s != 0:
             menu()
         
       
#funcion para ver los libros registrados

def ver_libros_reg():
    print('\n******************AQUI PUEDES VER LIBROS REGISTRADOS******************')
    for l in lista:
    print (l.ids, "-" ,l.título, "-" ,l.género, "-" ,l.isbn, "-" ,l.editorial, "-" ,l.autores)

      s = input("presione cualquier tecla para volver al menú principal: ")
      print("")

    while s != 0:
        menu()
      
      
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
    
    s = input("presione cualquier tecla para volver al menú principal: ")
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
        print("3. Agregar informacion de un nuevo libro")
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
            print('Programa finalizado. Hasta la proxima!!')
            selec = False
        else:
            print('\nAsigne un valor valido\n')
            input('Presione enter para continuar')
            selec = True

def main():
    menu()
if __name__ == '__main__':
    main()
