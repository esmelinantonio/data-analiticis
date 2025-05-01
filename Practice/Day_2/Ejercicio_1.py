# Creación de tuplas
# Crea una tupla llamada coordenada que contenga la latitud y la longitud de Bogotá (4.7110,-74.0721).
# Imprime la tupla y accede a cada elemento por índice.

coordenada = (4.7110,-74.0721)
print(coordenada)

# Inmutabilidad
# Intenta cambiar el primer elemento de coordenada a 0.0.
# Observa el error que obtienes y escribe en un comentario por qué ocurre.
# coordenada[0]= 0.0
# print(coordenada)
# print('tuple object does not support item assignment')

# Desempaquetado
# Dada la tupla punto = (10, 20, 30),
# desempáquetala en tres variables x, y, z y muestra sus valores.
punto = (10, 20, 30)
x,y,z = punto
print(x,y,z)

# Longitud y pertenencia
# Crea un set llamado frutas = {"mango", "piña", "papaya"}.
# Verifica si "piña" está en el set y muestra la longitud total del set.
frutas = {"mango", "piña", "papaya"}


# Conversión lista→set / set→lista
# Convierte la lista numeros = [1, 2, 2, 3, 4, 4, 4, 5] a un set para eliminar duplicados.
# Luego vuelve a convertir el set resultante en lista y ordénala ascendentemente.

numeros = [1, 2, 2, 3, 4, 4, 4, 5]
set_numeros = set(numeros)
print(set_numeros)
num_lista = list(set_numeros)
num_lista.sort()
print(num_lista)



