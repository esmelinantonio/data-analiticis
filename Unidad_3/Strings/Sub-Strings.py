

saludo = "hola_Mundo"
# print(saludo[5:10])  # arranca desde el indice numero 2 y llega hasta el elemento numero 6
# print(saludo[3::3]) # trae los elementos desde la el indice en
# print(saludo[::-1])

# Ejemplos
texto = "ABCDEFGHIJKLMNOPQRSTU"
fragmento = texto[2]
print(fragmento) #C

fragmento = texto[2:5]
print(fragmento)

fragmento = texto[2:]
print(fragmento)

fragmento = texto[:2]
print(fragmento)

fragmento = texto[2:10:2]
print(fragmento)

fragmento = texto[::3]
print(fragmento)

fragmento = texto[::-1]
print(fragmento)

fragmento = texto[::-2]
print(fragmento)

# Ejercicos Sub-Strings
frase = "Controlar la complejidad es la esencia de la programación"
fragmento1 = frase[0:9]
print(fragmento1)

frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento1 = frase2[9::3]
print(fragmento1)

frase3 = "Es genial trabajar con ordenadores. No discuten,lo recuerdan todo y no se beben tu cerveza"
fragmento1 = frase3[::-1]
print(fragmento1)

# Métodos de String

x = "hola hola mundo".count("hola")
print(x)
x = "hola mundo".find("world")
print(x)

x = "C:/python36/python.exe".rfind("/")
print(x)

x = "Hola mundo".startswith("hola")
print(x)
