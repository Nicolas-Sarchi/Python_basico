# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir

print("\n\n")

def temperaturaMedia(temperaturaMax, temperaturaMin) :
    promedio =round((temperaturaMax + temperaturaMin) / 2 , 2)
    return promedio 

dias = int(input("Digite la cantidad de dias que desea introducir: "))

for i in range(dias):   
    temperaturaMax = float(input("\nTemperatura Máxima: "))
    temperaturaMin = float(input("Temperatura Mínima: "))
    
    print("El promedio de temperatura es: ", temperaturaMedia(temperaturaMax,temperaturaMin))
    

print("\n\n")

