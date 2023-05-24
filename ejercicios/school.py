
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
    }
}

dicMaterias = {
    1: {"nombre": "Matemáticas"},
    2: {"nombre": "Física"},
    3: {"nombre": "Lengua"},
    4: {"nombre": "Química"},
}

dicNotas = {
    1:{
    "idEstudiante": 1,
    "idMateria":1,
    "nota1":"p", 
    "nota2":"p", 
    "nota3":"p", 
    "notafinal":"p"
    }

}

def verMenu():
    os.system("cls") 
    print("********** COLEGIO **********\n")
    print('''Selecciones alguna de las siguientes opciones: 
    1. Notas        2. Estuiantes
    3. Materias     0. Salir''')

def verMenuMaterias(materias):
    os.system("cls") 
    print("********* MATERIAS *********\n")
    print("CÓDIGO\t\t\tNOMBRE")
    for materia in materias:
        print(materia,"\t\t\t",materias[materia]["nombre"])
    print('''Seleccione alguna de las siguientes opciones: 
    1. Crear        2. Editar
    3. Eliminar     0. Salir''')

def menuEstudiantes(estudiantes):
    os.system("cls") 
    print("******** ESTUDIANTES ********\n")
    print("CÓDIGO\t\t\tNOMBRE\t\t\tAPELLIDO\t\t\tCORREO")
    for estudiante in estudiantes :
        print(estudiante,"\t\t\t",estudiantes[estudiante]["nombre"],"\t\t\t",estudiantes[estudiante]["apellido"],"\t\t\t", estudiantes[estudiante]["correo"])
    print('''Seleccione alguna de las siguientes opciones: 
        1. Crear        2. Editar
        3. Eliminar     0. Salir''')
    
def menuMateriasN(opt):
    os.system("cls")
    if opt == 1:
        mat = "MATEMÁTICAS" 
    elif opt == 2:
        mat = "FISICA"
    elif opt == 3:
        mat = "LENGUA"
    elif opt == 4:
        mat = "QUIMICA"
    else:
         print("OPCION INVALIDA")
         
    print("*********", mat, "*********\n")
    print("""Qué desea hacer: 
          1. Agregar Nota     2. Editar Nota
          3. Eliminar Nota    4. Ver Notas
          0. Salir""")

def contarId(diccionario):
     id = list(diccionario.keys())[len(diccionario)] 
     return id 

def agregarMateria(id, nombre):
     dicMaterias[id] = {"nombre": nombre}

def agregarEstudiante(id):    
    dicEstudiantes[id] = {"nombre": nombre, "apellido": apellido, "correo": correo}
    
def verNotasMateria(estudiantes, materia):    
        print("CÓDIGO\t\t\tNOMBRE\t\t\tNOTA 1\t\t\tNOTA 2\t\t\tNOTA 3\t\t\tNOTA FINAL")
        for i in range(id):
            for estudiante in dicNotas :
                print(estudiante,"\t\t\t",estudiantes[estudiante]["nombre"],"\t\t\t",dicNotas[materia]["nota1"],"\t\t\t", dicNotas[materia]["nota2"],"\t\t\t", dicNotas[materia]["nota3"],"\t\t\t", dicNotas[materia]["notafinal"])
                

def crearNotaa():
    x = 0
        
        
        

def crear_id(diccionario):
    id = list(diccionario.keys())[len(diccionario)-1]
    return id + 1    
    

verMenu()
opcMenu = input()
while opcMenu != "0":

    if opcMenu == "1":
        os.system('cls')
        print("********* NOTAS *********\n")
        print('''Selecciones alguna de las siguientes opciones: 
                1. Matemáticas        2. Física
                3. Lenguaje           4. Química
                0. Salir''')
        id = int(input())
        dicNotas[id] = dicNotas[1]


        menuMateriasN(id)
            
        option = int(input())
        if option == 1:
                verNotasMateria(dicEstudiantes,id) 
                print("Digite el id de l estudiante al que quiere agregar la nota")

                idEstudiante = int(input())
    elif opcMenu == "2":

        
        menuEstudiantes(dicEstudiantes)
        opt = input()


        if opt == "1":

                print("********* AGREGAR *********\n")
                id = crear_id(dicEstudiantes)
                print("Por favor ingrese el nombre del nuevo estudiante: ")
                nombre = input()
                print("Por favor ingrese el apellido del nuevo estudiante: ")
                apellido = input()
                print("Por favor ingrese el correo del nuevo estudiante: ")
                correo = input()
                agregarEstudiante(id)
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
                        dicEstudiantes[id]["nombre"] = input()
                        # menuEstudiantes(dicEstudiantes)
                        print(dicEstudiantes)
                elif edit == 2:
                        print("Por favor ingrese el nuevo apellido del estudiante: ")
                        dicEstudiantes[id]["apellido"] = input()
                        # menuEstudiantes(dicEstudiantes)

                elif edit == 3:
                        print("Por favor ingrese el nuevo correo del estudiante: ")
                        dicEstudiantes[id]["correo"] = input() 
                        # menuEstudiantes(dicEstudiantes)
                else :
                        # menuEstudiantes(dicEstudiantes)          
                        print("cp")

        elif opt== "3":

                print("******** ELIMINAR ********\n")
                print("Por favor ingrese el código del estudiante a eliminar: ")
                id = int(input())
                del(dicEstudiantes[id]) 
                menuEstudiantes(dicEstudiantes)
        elif opt== "0":
                verMenu()
                opt = input ()    

    elif opcMenu == "3":
        print("********* MATERIAS **********\n")
        verMenuMaterias(dicMaterias)
        opc = input()
        
        if opc == "1":
                print("********* AGREGAR *********\n")
                id = crear_id(dicMaterias)
                print("Por favor ingrese el nombre de la nueva materia: ")
                nombre = input()
                agregarMateria(id, nombre)
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
                
        elif opc == "0":
                
            verMenu()
            opc = input ()
            
    else:
        print("Por favor, seleccione una opción válida\n")
        
        verMenu()
        opcMenu = input()

# dicNotas[idMateria]["nota1"], "\t\t\t", dicNotas[idMateria]["nota2"], "\t\t\t", dicNotas[idMateria]["nota3"], "\t\t\t", dicNotas[idMateria]["notafinal"]