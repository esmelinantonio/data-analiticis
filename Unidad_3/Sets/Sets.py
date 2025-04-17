# Metodos
mi_set_a = {1,2,"tres"}
mi_set_b = {3, "tres"}

# mi_set_a.add(5) # Agrega un elemento al set
# print(mi_set_a)

# mi_set_a.clear() # Remueve todos los elementos de un set
# print(mi_set_a)

# mi_set_c = mi_set_a.copy() # Retorna una copia del set
# print(mi_set_c)

#mi_set_c = mi_set_a.difference(mi_set_b) # Retorna el set formado por todos los elementos que UNICAMENTE existen el set A
# print(mi_set_c)

#mi_set_a.difference_update(mi_set_b) # remueve de A todos los elementos comunes a A y B
# print(mi_set_a)

# mi_set_a.discard("tres") # Remueve un elemento del set
# print(mi_set_a)

# mi_set_c = mi_set_a.intersection(mi_set_b) # Retorna el set formado por TODOS LOS ELEMENTOS que existen en A y B simultáneamente
# print(mi_set_c)

# mi_set_b.intersection_update(mi_set_a) # Mantiene unicamente los ELEMENTOS COMUNES a A y B
# print(mi_set_b)

# conjunto_disjunto = mi_set_a.isdisjoint(mi_set_b) # Devuelve True si A y B no tienen elementos en común
# print(conjunto_disjunto)

# es_subset = mi_set_b.issubset(mi_set_a) # Devuelve True si todos los elementos de B están presentes en A
# print(es_subset)

# es_superset = mi_set_a.issuperset(mi_set_b) # Devuelve True si A contiene TODOS los elementos de B
# print(es_superset)

# aleatorio = mi_set_a.pop() # Elimina y retoma un elemento al azar del set
# print(aleatorio)

# mi_set_a.remove("tres") # Elimina un item del set y arroja error si no existe
# print(mi_set_a)

mi_set_c = mi_set_b.symmetric_difference(mi_set_a) # Retorna todos los elementos de A y B excepto aquellos que son comunes a los dos
print(mi_set_c)

mi_set_b.symmetric_difference_update(mi_set_a) # Elimina los elementos comunes a A y B, agregando los que no están an presentes en ambos a la vez
print(mi_set_b)

mi_set_c = mi_set_a.union(mi_set_b) # Retorna un set resultado de combinar A y B (los datos duplicados se eliminan)
print(mi_set_c)

mi_set_a.update(mi_set_b) # Inserta en A los elementos de B
print(mi_set_a)













