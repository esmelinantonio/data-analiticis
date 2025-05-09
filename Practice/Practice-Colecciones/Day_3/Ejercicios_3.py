# 4 tuplas
un_elemento = ((5))
# print(type(un_elemento))

# Ejercicios de Set
colores = {"rojo", "verde", "azul"}
# print(type(colores))
colores.add("amarillo")
# print(colores)
colores.add("rojo")
# print(colores)
colores.remove("verde")
# print(colores)
# colores.remove("naranja")
# print(colores)
colores.discard("naranja")
# print(colores)
esta = "azul" in colores # Crea variable para consultar
# print(esta)

# Ejercicios set 2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# set3 = set1.union(set2)
# print(set3)
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1.difference(set2)
# print(set3)
# set3 = set1.symmetric_difference(set2)
# print(set3)

# Eliminar Duplicados de una Lista
numeros_duplicados = [1, 2, 2, 3, 4, 4, 5]
nueva = set(numeros_duplicados)
print(nueva)

