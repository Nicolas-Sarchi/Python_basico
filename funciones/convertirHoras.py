# Escribir dos funciones que permitan calcular:

# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

print("\n\n")

def segundosaHoras(segundos):
    seg =round(segundos % 60)
    minutos = round(segundos / 60)
    horas = round(segundos / 3600)
    
    return horas, minutos, seg

def horaaSegundos(horas, minutos, segundos):
    hr = horas * 3600
    minute = minutos * 60
    seconds = hr + minute + segundos
    return seconds
    
eleccion = int(input("Escoja: \n1. Convertir segundos a horas, minutos y segundos \n2. Horas, minutos y segundos a segundos\n"))

if eleccion == 1:
    segundos = int(input("Ingrese la cantidad de segundos que desea convertir: "))

    print("El resultado de la conversión de ",segundos," a Horas minutos y segundos respectivamente es: ", segundosaHoras(segundos))

elif eleccion == 2:
    horas = int(input("Ingrese la cantidad de horas que desea convertir: "))
    minutos = int(input("Ingrese la cantidad de minutos que desea convertir: "))
    segundos = int(input("Ingrese la cantidad de segundos que desea convertir: "))
    
    print (horas, " horas ", minutos, " minutos y ", segundos, " segundos convertidos a segundos es igual a: ", horaaSegundos(horas, minutos, segundos), "segundos")
    
else:
    print("Opción inválida")    
    




    

print("\n\n")
