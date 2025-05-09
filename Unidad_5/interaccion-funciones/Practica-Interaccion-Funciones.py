from  random import *

def lanzar_dados():
      dado_1 = randint(1,6)
      dado_2 = randint(1,6)
      return dado_1,dado_2

def evaluar_jugada(d1,d2):
    suma_dados = d1 + d2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados >6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
        
d1,d2 = lanzar_dados()
print(f"Tu lanzamiento es {d1} : {d2}")
print(evaluar_jugada(d1,d2))
    

lista_numeros =[]
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio

unica = reducir_lista([1, 2, 2, 3, 4, 4, 4, 5])
prom = promedio(unica)
print(f"Lista ordenada y sin duplicados: {unica}")
print(f"Promedio de elementos: {prom}")



lista_numeros = []
def lanzar_moneda():
    resultado = random.choice(["Cara", "Sello"])
    return resultado

def probar_suerte(moneda, lista_numeros):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Sello":
        print("La lista fue salvada")
        return lista_numeros


moneda = lanzar_moneda()
print(probar_suerte(moneda,[1, 2, 2, 3]))

   
    