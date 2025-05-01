# 1. Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
# cont = 10
# while cont >= 0:
#     print(cont)
#     cont -= 1

# Ejercicio Loop-While 2
# numeros = 50
# while numeros >= 0:
#    if numeros % 5 == 0:
#         print(numeros)
#    numeros -= 1

# Ejercicio Loop-While 3

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num <0:
        break
    print(num)
