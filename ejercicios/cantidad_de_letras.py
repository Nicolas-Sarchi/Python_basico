# Dada una lista con nombres completos de personas, realizar un programa que genere una segunda con la cantidad de palabras de cada uno de los nombres. La lista de nombres debe llenarse a través de nombres que se ingresan por teclado, hasta que el nombre ingresado sea “FIN” Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada nombre.

print("\n\n")
nombres = []
cantidadPalabras = []

nombre = input("Ingrese su nombre completo: ")


while nombre != "fin":
    nombres.append(nombre)
    cantidadPalabras.append(len(nombre.split()))
    nombre = input("Ingrese su nombre completo: ")

print("\nLa lista de nombres es: ", nombres)

print("\nLa cantidad de palabras respectivas para cada nomre es: ", cantidadPalabras)





print("\n\n")
