# Ejercicios Métodos de Strings

# Une la siguiente lista en un string, separando cada elemento con un
# espacio. Utiliza el método apropiado de listas/strings, y muestra en
# pantalla el resultado.
# lista_palabras = ["La","legibilidad","cuenta."]

lista_palabras = ["La","legibilidad","cuenta."]
x = " ".join(lista_palabras)
print(x)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
x = frase.replace("difícil","facil")
y = frase.replace("mala","buena")
print(frase)
print(x)
print(y)
z = len(frase)
print(z)


# Ejercicios Propiedades de Strings
Repe = "Repeticion\n" *15

print(Repe)

texto = "Tierra mojada,\nMis recuerdos de viaje\nEntra las lluvias"
text = "agua" in texto
print(text)

palabra = "electroencefalografista"
largo = len(palabra)
print(largo)
