
print("\n\n")
import os

dicEstudiantes = {
    1: {
    "nombre": "aa",
    "apellido": "aa",
    "correo": "a@abcd.com",
    },
    2: {
    "nombre": "bb",
    "apellido": "bb",
    "correo": "b@abcd.com",
    },
    3: {
    "nombre": "cc",
    "apellido": "cc",
    "correo": "c@abcd.com",
    },
    4: {
    "nombre": "dd",
    "apellido": "dd",
    "correo": "d@abcd.com"
    },
}

dicMaterias = {
    1: {"nombre": "Matemáticas"},
    2: {"nombre": "Física"},
    3: {"nombre": "Lengua"},
    4: {"nombre": "Química"},
}

def verMenu():
    os.system("clear") 
    print("********** COLE **********\n")
    print('''Selecciones alguna de las siguientes opciones: 
    1. Notas        2. Estuiantes
    3. Materias     0. Salir''')


  

def verMenuMaterias(materias):
    os.system("clear") 
    print("********* MATERIAS *********\n")
    print("CÓDIGO\t\t\tNOMBRE")
    for materia in materias:
        print(materia,"\t\t\t",materias[materia]["nombre"])
    print('''Seleccione alguna de las siguientes opciones: 
    1. Crear        2. Editar
    3. Eliminar     0. Salir''')

def menuEstudiantes(estudiantes):
    os.system("clear") 
    print("******** ESTUDIANTES ********\n")
    print("CÓDIGO\t\t\tNOMBRE\t\t\tAPELLIDO\t\t\tCORREO")
    for estudiante in estudiantes :
        print(estudiante,"\t\t\t",estudiantes[estudiante]["nombre"],"\t\t\t",estudiantes[estudiante]["apellido"],"\t\t\t", estudiantes[estudiante]["correo"])
    print('''Seleccione alguna de las siguientes opciones: 
        1. Crear        2. Editar
        3. Eliminar     0. Salir''')

verMenu()
opcMenu = input()
while opcMenu != "0":

    if opcMenu == "1":
        print("********* NOTAS *********\n")


    elif opcMenu == "2":

        print("******** ESTUDIANTES ********\n")
        menuEstudiantes(dicEstudiantes)
        opt = input()

        while opt != "0":

            if opt == "1":

                print("********* CREAR *********\n")
                id = list(dicEstudiantes.keys())[len(dicEstudiantes)-1]+1
                print("Por favor ingrese el nombre del nuevo estudiante: ")
                nombre = input()
                print("Por favor ingrese el apellido del nuevo estudiante: ")
                apellido = input()
                print("Por favor ingrese el correo del nuevo estudiante: ")
                correo = input()
                dicEstudiantes[id] = {"nombre": nombre, "apellido": apellido, "correo": correo}
                menuEstudiantes(dicEstudiantes)
                  
                

            elif opt == "2":

                print("********* EDITAR *********\n")
                print("Por favor ingrese el código del estudiante que desea editar: ")
                id = int(input())
                print('''Que quiere editar: 
                        1. Nombre       2. Apellido
                        3. Correo       0. Salir''')
                edit = int(input())

                if edit == 1:
                        print("Por favor ingrese el nuevo nombre del estudiante: ")
                        dicMaterias[id]["nombre"] = input()
                        menuEstudiantes(dicEstudiantes)
                elif edit == 2:
                        print("Por favor ingrese el nuevo apellido del estudiante: ")
                        dicMaterias[id]["apellido"] = input()
                        menuEstudiantes(dicEstudiantes)

                elif edit == 3:
                        print("Por favor ingrese el nuevo correo del estudiante: ")
                        dicMaterias[id]["correo"] = input() 
                        menuEstudiantes(dicEstudiantes)
                          

            elif opt== "3":

                print("******** ELIMINAR ********\n")
                print("Por favor ingrese el código del estudiante a eliminar: ")
                id = int(input())
                del(dicEstudiantes[id])  
                menuEstudiantes(dicEstudiantes)
            else:
                print("Por favor, seleccione una opción válida\n")
                menuEstudiantes(dicEstudiantes)
                opt = input ()    

    elif opcMenu == "3":
        print("********* MATERIAS **********\n")
        verMenuMaterias(dicMaterias)
        opc = input()
        while opc != "0":
            if opc == "1":
                print("********* CREAR *********\n")
                id = list(dicMaterias.keys())[len(dicMaterias)-1]+1
                print("Por favor ingrese el nombre de la nueva materia: ")
                nombre = input()
                dicMaterias[id] = {"nombre": nombre}
            elif opc == "2":
                print("********* EDITAR *********\n")
                print("Por favor ingrese el código de la materia a editar: ")
                id = int(input())
                print("Por favor ingrese el nuevo nombre de la materia: ")
                dicMaterias[id]["nombre"] = input()
            elif opc== "3":
                print("******** ELIMINAR ********\n")
                print("Por favor ingrese el código de la materia a eliminar: ")
                id = int(input())
                del (dicMaterias[id])
                
            
    else:
        print("Por favor, seleccione una opción válida\n")
        
        verMenu()
        opcMenu = input()
