# Crear y Acceder:
# Crea una lista llamada frutas con los siguientes elementos: "manzana", "banana", "cereza", "dátil".
# Imprime el segundo elemento de la lista.
# Imprime el último elemento de la lista utilizando indexación negativa.

frutas = ["manzana", "banana", "cereza", "dátil"]
# print(type(frutas))
print(frutas[2])
print(frutas[-1])

# Modificar Elementos:
# En la lista frutas, cambia "banana" por "arándano".
# Imprime la lista modificada.
frutas[1] = "arándano"
print(frutas)

# Agregar y Eliminar Elementos:
frutas.append("kiwi") # Agrega "kiwi" al final de la lista frutas.
frutas.insert(1,"pera") # Inserta "pera" en la segunda posición de la lista.
frutas.remove("cereza") # Elimina "cereza" de la lista.
print(frutas) # Imprime la lista después de estas operaciones.

# Sublistas (Slicing):
# Crea una nueva lista llamada primeras_tres_frutas que contenga los primeros tres elementos de la lista frutas.
# Crea una nueva lista llamada ultimas_dos_frutas que contenga los últimos dos elementos de la lista frutas.
# Imprime ambas sublistas.
primeras_tres_frutas = frutas[:3]
ultimas_dos_frutas = frutas[3:]
print(primeras_tres_frutas,ultimas_dos_frutas)

