# Se realiza la compra de N artículos, en donde se ingresa el código del artículo y la cantidad y
# mediante el uso de diccionarios para los nombres y valores unitarios de los artículos, el
# programa debe obtener el nombre de cada artículo, cantidad comprada, valor unitario, valor
# total de acuerdo a la cantidad comprada y finalmente calcular el valor total de la compra.
# Se suministra el diccionario de nombres de artículo y otro con los valores unitarios.
# articulos={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
# valores={1:2500,2:3800,3:1200,4:35000,5:3700}


print ("\n\n")

articulos = {

    1:"Lapiz",
    2:"Cuadernos",
    3:"Borrador",
    4:"Calculadora",
    5:"Escuadra"
    
    }

valores = {
    1:2500,
    2:3800,
    3:1200,
    4:35000,
    5:3700
    }

compra = {}
valorTotal = 0

while True :
    codigo = int(input("\nDigite el còdigo del producto que desea comprar (Digite 0 para salir): "))
    if codigo == 0 :
        break
    cantidad = int(input("\nDigite la cantidad del producto que desea comprar: "))
    nombre = articulos.get(codigo)
    valor_unitario = valores.get(codigo)
    valorTotalArt = cantidad * valor_unitario
    valorTotal += valorTotalArt

    compra[nombre] = {"Cantidad" : cantidad, "Valor Unitario" : valorTotalArt, "Valor Total" : valorTotal}


for nombre, i in compra.items():
    print ("\nArtìculo: ", nombre)
    print("Cantidad comprada: ", i["Cantidad"], "\t\tValor unitario: " , i["Valor Unitario"], "\t\tValor total: ", i["Valor Total"])


print ("\nVALOR TOTAL DE LA COMPRA: ", valorTotal)    






print ("\n\n")
