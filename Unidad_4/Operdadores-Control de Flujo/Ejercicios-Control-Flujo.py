# Ejercicio 1 de Control de flujo
# Utilizando las variables num1 y num2, que se alimentan con el input del
# usuario (tal como en el código ya proporcionado):
# Crea una estructura de control de flujo que compare los valores de las
# variables, y arroje un resultado de acuerdo al caso:
#  "num1 es mayor que num2"
#  "num2 es mayor que num1"
#  "num1 y num2 son iguales"
# Debes mostrar en pantalla el valor de las variables ingresadas en lugar de
# num1 y num2.
#
# num1 = input("Digite un numero")
# num2 = input("Digite un numero")

# if num1 > num2:
#  print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#  print(f"{num2} es mayor que {num1}")
# else:
#  print(f"{num1} y {num2} son iguales")

# Ejercicio 2 de Control de flujo
# persona = 16
# licencia = False
#
# if persona <= 16 and licencia:
#  print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# elif persona >= 18 and licencia:
#  print("Puedes conducir")
# else:
#  print("No puedes conducir. Necesitas contar con una licencia")

# Ejercicio 3 de Control de flujo

programa_python = False
sabe_ingles = False

if programa_python and sabe_ingles:
 print("Cumples con los requisitos para postularte")
elif not programa_python and  not sabe_ingles:
 print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif programa_python or sabe_ingles:
 print("Para postularte, necesitas tener conocimientos de inglés")
else:
 print("Para postularte, necesitas saber programar en Python")


