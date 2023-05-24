# CREAR DICCIONARIOS PARA ALMACENAR INFORMACION
import os
import time
opc = ""
infEstudiantes = {
    1:{
    "nom":"camilo",
    "apll":"Sanchez",
    "mail":"accurrea@gmail.com"
    },
    2:{
    "nom":"julian",
    "apll":"currea",
    "mail":"julian@gmail.com"
    },
    3:{
    "nom":"nico",
    "apll":"arias",
    "mail":"nico@gmail.com"
    },
    4:{
    "nom":"jazon",
    "apll":"rodrigues",
    "mail":"jazon@gmail.com"
    },
    5:{
    "nom":"daniel",
    "apll":"camargo",
    "mail":"daniel@gmail.com"
    },
}
dic_materias = {
    1:{"nomM":"Matematicas"},
    2:{"nomM":"fisica"},
    3:{"nomM":"sociales"},
    4:{"nomM":"artes"},
    5:{"nomM":"Quimica"},
    6:{"nomM":"Informatica"},
    7:{"nomM":"Deporte"},
}

#LISTA NOTAS MATERIA
dic_notas = {
    1:{
    "idEstudiante":1,
    "idMateria":1,
    "nota1":0,
    "nota2":0,
    "nota3":0,
    "notafinal":0
    }
}
def menu():
    os.system("clear")
    print("**********I.E.D XYZ********")
    print("""Seleccione una opcion
        1. NOTAS       2. ESTUDIANTES
        3. MATERIAS   4. SALIR""")
#FUNCION MENU MATERIAS:
def menu_m(diccionarioM):
    os.system("clear")
    print("**********MATERIAS********")
    v_materia(diccionarioM)
    print("""Seleccione una opcion
        1. AGREGAR       2. MODIFICAR
        3. ELINAR   4. SALIR""")
# FUNCION MENU ESTUDIANTES
def m_estudiantes():
    os.system("clear")
    print("********MENU ESTUDIANTES********")
    print("""SELECCIONE UNA OPCION
    1. AGREGAR ESTUDIANTE      2. MODIFICAR ESTUDIANTE
    3. ELIMINAR ESTUDIANTE     4. LISTA
    5. SALIR""")
#FUNCION MENU MODIFICAR ESTUDIANTE
def menu_m_estudiante():
    os.system("clear")
    print("*************MENU MODIFICACION DE ALUMNO****************")
    print("""SELECCIONE UNA OPCION
    1. MODIFICAR NOMBRE       2. MODIFICAR CORREO
    3. SALIR""")
# FUNCION MENU AGREGAR NOTAS
def menu_notas():
    os.system("clear")
    print("*************MENU MATERIAS***************")
    print("""SELECCIONE UNA OPCION
    1. AGREGAR ESTUDIANTE       2. MODIFICAR NOTAS
    3. VER LISTA""")
# FUNCION AGREGAR MATERIA
def agregar_materia(materias,nombre):
    id = crear_id(materias)
    materias[id] = {
        "nomM":nombre
    }
    return materias
#FUNCION AGREGAR ESTUDIANTES
def agregar_estudiante(diccionario_e, nombre_e,apell_e,maill_e):
    id = crear_id(diccionario_e)
    diccionario_e[id] = {
        "nom": nombre_e,
        "apll": apell_e,
        "mail": maill_e
    }
    return diccionario_e
#FUNCION AGREGAR ESTUDIANTES Y NOTAS AL DICCIONARIO DE "dic_notas"
def agregar_est_materia(dicN,codE,codM):
    id = crear_id(dicN)
    dicN[id]={
        "idEstudiante":codE,
        "idMateria":codM,
        "nota1":"P",
        "nota2":"P",
        "nota3":"P",
        "notaFinal":"P"
    }   
#FUNCIOM MODIFICAR NOTAS
def modificar_notas(dic,a,b,c,cl,cl2,dic2):
    dic[cl]={
        dic2[cl2]:{
        "n1": a,
        "n2": b,
        "n3": c
    }
    }
#FUNCION CREAR ID
def crear_id(diccionario):
    id = list(diccionario.keys())[len(diccionario)-1]
    return id + 1
#FUNCION VER MATERIAS
# def ver_materias(materias):
#     lisMaterias = "CODIGO\t\tMATERIA\n"
#     for i in materias:
#         lisMaterias += str(i) + "\t\t" + materias[i]["nomM"] + "\n"
#     return lisMaterias
def v_materia(dic):
    print("CODIGO\t\tMATERIA\n")
    for i in dic:
        dic1 = dic[i]["nomM"]
        print(f"{i}\t\t{dic1}")
#FUNCION MOSTRAR LISTA DE ESTUDIANTES
def mostrar_est(dicc):
    print("CODIGO\t\tNOMBRE\t\tAPELLIDO\t\tMAIL")
    for i,j in dicc.items():
        n = j["nom"]
        a = j["apll"]
        c = j["mail"]
        print(f"{i}\t\t{n}\t\t{a}\t\t{c}")

# FUNCION PARA MOSTRAR LISTADO DE ESTUDIANTES CON LADS NOTAS
def materia_listado(d,cod):
    print("NOMBRE\t\tMATERIA\t\tN1\t\tN2\t\tN3\t\tNF")    
#TODO: DESDE ACA EMPIEZA EL PROGRAMA 
menu()
opc = input("Opcion: ")
while opc != "0":
    if opc == "1":
        menu_notas()
        opc = input("Opcion: ")
    elif opc == "2":
        m_estudiantes()
        opc = input("Opcion: ")
        while opc != "5":
            if opc == "1":
                print("*********AGREGE ESTUDIANTES********")
                n_nombre1 = input("Ingrese nombre estudiante nuevo: ")
                n_apellido1 = input("Ingrese apellido estudiante nuevo: ")
                n_mail1 = input("Ingrese mail estudiante nuevo: ")
                agregar_estudiante(infEstudiantes,n_nombre1,n_apellido1,n_mail1)
                print("estudiante agregado correctamente")
                mostrar_est(infEstudiantes)
                time.sleep(1)
            elif opc == "2":
                menu_m_estudiante()
                opc = input("Opcion: ")
                mostrar_est(infEstudiantes)
                cod_e = int(input("Ingrese codigo estudiante: "))
                while opc != "3":
                    if opc == "1":
                        print("******MODIFICACION NOMBRE******")
                        nombre_n = input("Ingrese nombre nuevo: ")
                        apellido_n = input("ingrese nuevo apellido: ")
                        infEstudiantes[cod_e] = {
                            "nom": nombre_n,
                            "apll": apellido_n
                        }
                        print("modificacion exitosa")
                        time.sleep(1)
                    elif opc == "2":
                        print("*****MODIFICACION CORREO*******")
                        correo_n = input("Ingrese correo nuevo: ")
                        infEstudiantes[cod_e] = {
                            "mail": correo_n
                        }
                        print("Modificacion exitosa")
                        time.sleep(1)
                    menu_m_estudiante()    
                    opc = input("Opcion: ")
                    cod_e = int(input("Ingrese codigo estudiante: "))
            elif opc == "3":
                print("**********ELIMINAR ESTUDIANTE************")
                mostrar_est(infEstudiantes)
                cod_del = int(input("Ingrese codigo estudiante: "))
                del infEstudiantes[cod_del]
                mostrar_est(infEstudiantes)
                print("Estudiante eliminado correctamente")
                time.sleep(2)
            elif opc == "4":
                print("************LISTADO DE ESTUDIANTES*************")
                mostrar_est(infEstudiantes)
                time.sleep(2)
            m_estudiantes()
            opc = input("Opcion: ")
        time.sleep(1)
    elif opc == "3":
        menu_m(dic_materias) 
        opc = input("opcion.")
        while opc != "4":
            if opc == "1":
                print("**********AGREGAR MATERIA***********")
                nombre1 = input("Ingrese nombre materia: ")
                agregar_materia(dic_materias,nombre1)
                print("Materia agregada exitosamente")
                time.sleep(2)
            elif opc == "2":
                print("*********MODIFICAR MATERIA*************")
                clave = int(input("ingrese clave: "))
                n_mombre=input("Ingrese nuevo nombre: ")
                dic_materias[clave]={
                    "nomM":n_mombre
                }
                print("***materia modificada exitosamente***")
                time.sleep(2)
            elif opc == "3":
                print("*******ELIMINAR MATERIA********")
                clave_e = int(input("Ingrese clave materia que decea eliminar: "))
                del dic_materias[clave_e]
                print("****MATERIA ELIMINADA EXITOSAMENTE*****")
                time.sleep(2)
            menu_m(dic_materias)             
            opc = input("Opcion: ")
    elif opc == "4":
        print("Ingrese una opcion valida")
    menu()
    opc=input("opcion: ")