from random import *
intentos = 6
##############################################################
# elegir la palabra
def elegir_palabra():
    palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
    eleccion = choice(palabras)
    tamaño = len(eleccion)
    eleccion_lista =list(eleccion)

    return eleccion, tamaño, eleccion_lista
##################################################################


# def ocultar_palabra():
    palabra_oculta = " - "
    





# Pedir la letra
def pedir_letra():
    letra = str(input("Elige una letra: "))
    letra.lower()
    return letra
######################################################################

def comprobar(letra,eleccion_lista):
    indice = 0;
    for letra in eleccion_lista():
        print(indice,letra)
        indice += 1
    return indice


letra = pedir_letra()
lista = elegir_palabra()
# print(comprobar(letra,lista))

while intentos > 0:
    print("*" * 20,"\n")
    print(lista)
    print("Letras incorrectas:")
    print(f"Intentos: {intentos}")
    print("\n")
    # if letra in lista:

    print("*" * 20,"\n")
    pedir_letra()
    intentos = intentos - 1
    # comprobar(letra,eleccion_lista)







