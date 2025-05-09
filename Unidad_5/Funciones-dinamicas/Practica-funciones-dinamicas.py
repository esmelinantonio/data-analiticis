# Ejercicio 1
lista_numeros = []
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True
    
resultado = todos_positivos([1,2,3,4,-5])
print(resultado)

# Ejercicio 2
lista_numeros = []
def suma_menores(lista_numeros):
    cont = 0
    for n in lista_numeros:
        if n in range(1,100):
            cont += n
    return cont

resultado = suma_menores([1,2,3,4,5])
print(resultado)

# Ejercicio 3
lista_numeros = []
def cantidad_pares(lista_numeros):
    cont = 0
    for n in lista_numeros:
        if n % 2 == 0:
            cont += 1
    return cont

resultado = cantidad_pares([1,2,3,4,5])
print(resultado)
