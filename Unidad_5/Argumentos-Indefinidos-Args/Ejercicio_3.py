def numeros_persona(name, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return f"{name} la suma de tus numeros es {suma_numeros}"

res = numeros_persona("esmelin", 1,2,3,4,5)
print(res)