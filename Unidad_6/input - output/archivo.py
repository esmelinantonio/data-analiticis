archivo = open('archivo.txt')

# print(archivo)
# # print(archivo.read())
# print(archivo.readline())
#-------------------------------------------------
# una_linea = archivo.readline()
# print(una_linea)
#
# una_linea = archivo.readline()
# print(una_linea)
#
# una_linea = archivo.readline()
# print(una_linea)
#---------------------------------------------------
# una_linea = archivo.readline()
# print(una_linea.upper())
#
# una_linea = archivo.readline()
# print(una_linea.rstrip())
#
# una_linea = archivo.readline()
# print(una_linea)
lineas = archivo.readlines()
for linea in lineas:
    print("Aqui dice: " + linea)
    
print(lineas)
archivo.close()
