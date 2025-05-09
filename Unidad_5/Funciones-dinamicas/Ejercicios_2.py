

def chequear_3_cifras(lista):
    lista_vacia = []
    for n in lista:
        if n in range(100,1000):
            lista_vacia.append(n)
        else:
            pass
    return lista_vacia

resultado = chequear_3_cifras([50,80,125,500])
print(resultado)