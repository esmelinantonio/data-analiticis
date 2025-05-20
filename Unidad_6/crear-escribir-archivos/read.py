# archivo = open('test.txt', 'r')
# archivo.write('Linea 4')
# archivo.close()


# Abre o crea un archivo (si no existe previamente) en modo de
# escritura, lo que significa que cualquier contenido previo se sobrescribirá.
archivo = open('read.txt', 'w')
archivo.write('Linea 4')
archivo.close()


# Abre el archivo para añadir líneas a continuación de la última que
# ya exista en el mismo. Crea un archivo en caso de que el mismo no exista
archivo = open('read.txt', 'a')
archivo.write('Linea 5')
archivo.close()

archivo = open('read.txt', 'w')
archivo.write('Linea 1\n')
archivo.write('Linea 2\n')
archivo.close()

archivo = open('read.txt', 'w')
archivo.write('''Linea 1
Linea 2
Linea 3
''')
archivo.close()

archivo = open('read.txt', 'w')
lista = ['Linea 1','Linea 2','Linea 3','Linea 4']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

