lista_1 = ["C","C++","Python","Java"]
lista_2 = ["PHP", "SQl", "VBA","JavaScript"]

print(lista_1[1:3]) # indexado
print(len(lista_1)) # cantidad de elementos
print(lista_1 + lista_2) # concatenación

lista_1.append("R") # Agrega un elemento a la ultima posicion de la lista
print(lista_1)
eliminado = lista_1.pop(3) # elimina un elemento de la lista dado el índice, y devuelve el valor quitado.
print(lista_1)
print("Eliminado: " + eliminado)

lista_3 = ["d","a","c","b","e"]
lista_3.sort() # ordena los elementos de la lista en el lugar
print(lista_3)

lista_4 = [5,4,3,2,1]
lista_4.reverse() # invierte el orden de los elementos en el lugar
print(lista_4)