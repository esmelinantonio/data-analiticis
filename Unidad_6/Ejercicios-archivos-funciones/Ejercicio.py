import os
from pathlib import Path
def abrir_leer(archivo):
    archivo = open(archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido
# -----------------------------------------------------------
def sobrescribir():
    archivo = open('read.txt', 'w')
    archivo.write("contenido eliminado")
    archivo.close()

# ------------------------------------------------

def registro_error(archivo):
    archivo = open(archivo, 'a')
    actualizar = archivo.write('\nse ha registrado un error de ejecución')
    archivo.close()
    return actualizar
    


print(abrir_leer('read.txt'))
sobrescribir()
print(abrir_leer('read.txt'))
registro_error('read.txt')
print(abrir_leer('read.txt'))




