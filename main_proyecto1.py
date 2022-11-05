
















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
            basedatoss.to_string()
            print("Se han cargado los libros")
            input('presione enter para continuar')
            selec = True
        elif ingreso == '2':
            mostrar_libros_guardados()
            selec = True
        elif ingreso == '3':
            registrarlibro()
            ver_libros_reg()
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