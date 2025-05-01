lista = ['a','b','c']
for letra in lista:
    pos = lista.index(letra)+1
    print(f"posición {pos} = {letra}")
#--------------------------------------------------------------------
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

for letra in [1,2,3,4,5]:
    print(letra)

for letra in (1,2,3,4,5):
    print(letra)