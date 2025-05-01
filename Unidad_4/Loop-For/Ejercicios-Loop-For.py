 # Ejercicio 1
# alumnos_clase = ["María","José","Carlos","Martina","Isabel","Tomás","Daniela"]
# for alumno in  alumnos_clase:
#      print("Hola " + alumno)
#------------------------------------------------------
 # Ejercicio 2
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma_numeros = 0
# for numeros in lista_numeros:
#     suma_numeros += numeros
# print(suma_numeros)
#-----------------------------------------------------------
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

suma_pares = 0
suma_impares = 0
for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    elif num % 2 == 1:
        suma_impares += num
print(suma_pares)
print(suma_impares)
