# Se desea realizar un programa en el cual se ingresen números enteros, los cuales se deben almacenar en una lista. Se debe ingresar números hasta que el número ingresado sea 99999. Una vez creada la lista, se desea conocer cuales y cuántos son pares e impares.

print("\n\n")

numeros = []

numero = int(input("Ingrese un nùmero entero diferente a 99999, de lo contrario el programa finalizarà: "))

while numero != 99999:
    numeros.append(numero)
    numero = int(input("\nIngrese un nùmero entero diferente a 99999, de lo contrario el programa finalizarà: "))

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else : 
        impares.append(num)    

print ("\n\nLa cantidad de nùmeros pares es de: ", len(pares))
print ("\nLos nùmeros pares son:  ", pares)

print ("\nLa cantidad de nùmeros impares es de: ", len(impares))
print ("\nLos nùmeros impares son:  ", impares)




print("\n\n")
