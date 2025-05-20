from random import *
def saludar():
    print("¡Hola Mundo!")
saludar()


def bienvenida(nombre_persona = "Pedro"):
    print(f"¡Bienvenido {nombre_persona}!")
bienvenida()




def cuadrado(numero = randint(1,10)):
   print (f"la potencia de 2 del {numero} es: {numero ** 2}")
cuadrado()
