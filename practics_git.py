class Libro:
    def __init__(self):
     self.id = ()
     self.título = ("")
     self.género = ("")
     self.isbn = ()
     self.editorial = ("")
     self.autores = ("")
def menu() :
    selec = 0
    while selec != 4:
     print("Biendenidos al Registro de Libros")
     print("elija una de las opiones:")
     print("*******************************************")
     print("1. registrar el Libro")
     print("2. Ver libro")
     print("3. buscar libro")
     print("4. salir")
     selec = int(input("elija una opcion: "))
     if selec == 1:
        registrar()
    if selec == 2:
        mostrar()
    if selec == 3:
        buscar()
    if selec == 4:
        salir()
def registrar():
    print("esta es la funcion de registro")
    libro = Libro()
    libro.id = (input("introduzca el id del libro: "))
    libro.título = (input("introduzca el título del libro: "))
    libro.género= (input("introduzca a que género pertenece el libro: "))
    libro.isbn= (input("introduzca el isbn del libro: "))
    libro.editorial = (input("introduzca la editorial del libro: "))
    libro.autores = (input("introduzca el el autor o los autores del libro: 1"))

def mostrar():
    print("esta es la opcion para mostrar libros registrados")
def buscar():
    print("esta es la opcion para buscar un libro registrado")
def salir():
    print("gracias por usar este programa")

menu()





"""def _del_(self):
        return None
        def __i"""