def cantidad_atributos(**kwargs):
    suma = 0
    for k in kwargs.items():
        suma += 1
    return suma


kwargs = {'x':'uno','y':'dos','z':'tres'}
res = cantidad_atributos(**kwargs)
print(res)