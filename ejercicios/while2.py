print("\n\n")
print("****************************** OPERACIONES BÁSICAS  ****************************\n")
resultado = ""
otra = "s"

while otra.lower() == "s": 
    print("\nDigite la opción que desea calcular: \n\n 1. Sumar \n 2. Resta \n 3. Multiplicación \n 4. División") 
    operacion = input()

    if operacion == "1":
        sum1 = int(input(f"Ingrese el número 1: "))
        sum2 = int(input(f"Ingrese el número 2: "))
        suma = sum1 + sum2
        calculo = str(sum1) + " + " + str(sum2)
        print("\nLa suma de ", calculo, "es: ", suma)
        otra = input("\nDesea realizar otras operación? (s/n): ")

    elif operacion == "2":
        res1 = int(input(f"Ingrese el número 1: "))
        res2 = int(input(f"Ingrese el número 2: "))
        resta = res1 - res2
        calculo = str(res1) + " - " + str(res2)
        print("\nLa resta de ", calculo, "es: ", resta)
        otra = input("\nDesea realizar otras operación? (s/n): ")

    elif operacion == "3":
        mul1 = int(input(f"Ingrese el número 1: "))
        mul2 = int(input(f"Ingrese el número 2: "))
        multi = mul1 * mul2
        calculo = str(mul1) + " * " + str(mul2)
        print("\nLa multiplicación de ", calculo, "es: ", multi)
        otra = input("\nDesea realizar otras operación? (s/n): ")

    elif operacion == "4":
        div1 = int(input(f"Ingrese el número 1: "))
        div2 = int(input(f"Ingrese el número 2: "))
        divi = div1 / div2
        calculo = str(div1) + " / " + str(div2)
        print("\nLa división de ", calculo, "es: ", divi)
        otra = input("\nDesea realizar otras operación? (s/n): ")
    
    else:
        print("\nDigite una opción correcta")