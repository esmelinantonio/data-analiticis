# Pedir datos al usuario
nombre = input("Digite su Nombre: ")
apellido =input("Digite su Apellido: ")
edad = input("Digite su Edad: ")

# Convertir edad a String
nueva_edad  = str(edad)
# print(type(nueva_edad))

# Genera ID automático
automatic_id = nombre[0:3].upper()+nueva_edad
# print(automatic_id)

dic = {"nombre":nombre,"apellido":apellido,"edad":nueva_edad,"ID":automatic_id}
print(dic)

print(f"Cliente registrado:\nNombre completo: {nombre} {apellido}\nEdad: {nueva_edad}\nID generado: {automatic_id} ")

