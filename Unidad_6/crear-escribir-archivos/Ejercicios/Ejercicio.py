archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()

# ------------------------------------------------------
archivo = open('mi_archivo.txt', 'r')
# print(archivo.read())
archivo.close()

# ---------------------------------------------------------
archivo = open('mi_archivo.txt', 'a')
archivo.write('\nNuevo inicio de sesión')
archivo.close()
# ------------------------------------------------------
archivo = open('mi_archivo.txt', 'r')
# print(archivo.read())
archivo.close()
# ----------------------------------------------------------

archivo = open('registro.txt', 'w')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for valor in registro_ultima_sesion:
    archivo.writelines(valor + '\n')

archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()
