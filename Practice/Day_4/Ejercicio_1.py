from Practice.Day_1.Ejercicio_5 import palabra

nombre_completo = "Juan Perez"
print(len(nombre_completo))
print(nombre_completo[0].upper())
print(nombre_completo[9].lower())

frase = "Este Es Un Ejemplo."
print(frase.upper())
print(frase.lower())

texto = "El perro salta sobre la valla."
nuevo_texto = texto.replace("perro", "gato")
print(nuevo_texto)

fecha = "25/10/2023"
dia = print(fecha[0:2])
mes = print(fecha[3:5])
anio = print(fecha[6:])

palabra_1 = "Hola"
palabra_2 = "Mundo"
palabra = palabra_1 + " " + palabra_2
print(palabra)
print("Python"*3)

palabra = "Programacion"
print(palabra[3])
print(palabra[3:8])
print(palabra[0:5])
print(palabra[6:])
print(palabra[::-1])

frase_larga = "La programación con Python es divertida."
subcadena = "Python"
subcadena_no_existente = "Java"
search = frase_larga.find(subcadena)
search = frase_larga.find(subcadena_no_existente)
print(search)

texto_repetitivo = "banana"
repeat =texto_repetitivo.count("a")
print(f"El carácter 'a' aparece {repeat} veces.")

nombre_archivo = "reporte_final.txt"
name1 = nombre_archivo.startswith("reporte_")
name2 = nombre_archivo.endswith('.txt')
print(name1,name2)

producto = "Laptop"
precio = 1200
print(f"El producto {producto} tiene un precio de ${precio} ")