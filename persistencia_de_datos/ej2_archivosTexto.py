# Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
# El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 3. añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado en el archivo de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

print("\n\n")
import os

def crearArchivo():
    archivo = open("Directorio.txt", "w")
    clientes = "Cliente1, 3123455667\nCliente2,3245325423\nCliente3,1234556786"
    archivo.write(clientes)
    archivo.close()
    print("Archivo creado exitosamente")


def consultarCliente(nombreCliente):
    archivo = open("Directorio.txt", "r")
    clientes = archivo.readlines()
    for linea in clientes:
        if nombreCliente == linea:
            print(linea)
    archivo.close()

def addClient():
    archivo = open("Directorio.txt", "a")
    name = input("Nombre del cliente : ")
    tel = input("Teléfono : ")
   
   
   
    archivo.write(name)
    archivo.write(", ")
    archivo.write(tel)
    archivo.close()

def EliminarCliente(nombreCliente):
    archivo = open("Directorio.txt", "r")
    clientes = archivo.readlines()
    for linea in clientes:
        if nombreCliente == linea:
            del(linea)
           
    archivo.close()


def verMenu():
    print("\n============== DIRECTORIO TELEFÓNICO =================")
    print("1. Crear archivo")
    print("2. Consultar cliente")
    print("3. Añadir cliente")
    print("4. Eliminar cliente")
    print("5. Salir")


verMenu()

opc = int(input())

while opc!= 5:
    if opc == 1:
        crearArchivo()
        print("\n\n")

    elif opc == 2:
        consultarCliente(input("Nombre del cliente : "))

    elif opc == 3:
        addClient()

    elif opc == 4:
        EliminarCliente(input("Nombre del cliente : "))

    verMenu()
    opc = int(input())    
