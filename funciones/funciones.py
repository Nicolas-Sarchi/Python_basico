# Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

print ("\n\n")

def maxmin(numeros) :
    maximo = numeros[0]
    minimo = numeros[0]
    for i in range(1, cantidad):
        if numeros[i] > maximo:
            maximo = numeros[i]
            
        elif numeros[i] < minimo:
            minimo = numeros[i]
    
    return minimo , maximo
    
        
numeros = []

cantidad = int(input("Ingrese la cantidad de numeros que desea agregar a la lista: "))

for i in range(cantidad) :
    numero = int(input("\nIngrese un númeo: "))
    numeros.append(numero)
    
    
print("Los valores mínimo y máximo respectivamente son: " , maxmin(numeros))





print ("\n\n")
