import math

numeros = []
conteo_num = 0
suma_raices = 0


while True:
    try:
        num = int(input("Ingrese un nùmero entero (0 para terminar): "))

        if num == 0:
            break

        numeros.append(num)
        conteo_num += 1

    except ValueError :
        print("Error: Ingrese un nùmero estero vàlido")

for numero in numeros:
    try:
        raiz_cuadrada = math.sqrt(num)    
        suma_raices += raiz_cuadrada

    except ValueError:
        print("Error: no se puede calcular la raìz cuadrada de un nùmero negativo")


try :
    promedio_aritmetico = sum(numeros) / suma_raices

except ZeroDivisionError:
    print("Error: no se puede realizar una divisiòn por 0")    


print("Cantidad total de nùmeros ")






