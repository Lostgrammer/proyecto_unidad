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
