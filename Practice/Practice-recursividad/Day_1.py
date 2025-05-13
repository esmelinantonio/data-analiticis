# Suma de un numero
def sumarecursiva(num):
    if num == 1:
        return 1
    else:
        return num+sumarecursiva(num-1)
    
print(sumarecursiva(5))
print("----------------------------------------------------")
def sumarecursiva_2(num):
    if num > 0:
        result = num + sumarecursiva_2(num - 1)
        print(result)
    else:
        result = 0
    return result

sumarecursiva_2(6)
# Factorial de un numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(5))
print("----------------------------------------------------")
# Mostrar lista recursiva
def mostrarListaRec(lista, indice):
    if indice != len(lista):
        print(lista[indice])
        mostrarListaRec(lista,indice + 1)
        
lista = [1,2,3,4,5]
print(mostrarListaRec(lista,0))
print("----------------------------------------------------")




