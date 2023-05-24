
import json
lista = [1,2,3,4,5,6,7,8,9,10]


with open("./archivos/lista.json" ,"w") as archivo :
    json.dump(lista, archivo)

archivo.close()    