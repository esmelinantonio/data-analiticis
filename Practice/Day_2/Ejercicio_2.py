# Operaciones con sets
from os.path import altsep

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.union(B)
print(C)

C = A.intersection(B)
print(C)

C = A.difference(B)
print(C)

C = A.symmetric_difference(B)
print(C)

# Tuplas anidadas
rectangulo = ((0, 0), (10, 5))
(x1,y1),(x2,y2) = rectangulo

base = abs(x2 - x1)
altura = abs(y2 - y1)
area = base *altura
print(area)