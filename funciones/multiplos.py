

print("\n\n")

def esMultiplo(num1, num2):
    residuo = num1 % num2
    if residuo == 0:
        return True
    else :
        return False
    
num1 = int(input("Digite un número entero: "))  
num2 = int(input("Digite otro número entero: "))    

print("\n", num1, "Es múltiplo de ", num2 ,"? ", esMultiplo(num1, num2))

print("\n\n")
