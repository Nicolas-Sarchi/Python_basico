archivo_texto = open("./archivos/nombres.txt",  "r")

lista_nombres = archivo_texto.readlines()

archivo_texto.close()

print(lista_nombres)