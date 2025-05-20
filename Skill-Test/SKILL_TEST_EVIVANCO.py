texto = input("Ingresa un texto a elección: ").lower()
letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()
lista_texto = [letra1,letra2,letra3]

# TEXTO INVERTIDO

palabras = texto.split()
palabras_invertidas = palabras[::-1]
texto_invertido = " ".join(palabras_invertidas)

print("------------------------------------------------")
print(" \n"," \n"," \n")
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado la letra '{letra1}' repetida {texto.count(lista_texto[0])}")
print(f"Hemos encontrado la letra '{letra2}' repetida {texto.count(lista_texto[1])}")
print(f"Hemos encontrado la letra '{letra3}' repetida {texto.count(lista_texto[2])}")
print(" \n"," \n"," \n")
print("------------------------------------------------")
print(" \n"," \n"," \n")
print("CANTIDAD DE PALABRAS")
print(f"Hemos encontrado {len(texto)} palabras en tu texto")
print(" \n"," \n"," \n")
print("------------------------------------------------")
print(" \n"," \n"," \n")
print("LETRAS DE INICIO DE INICIO Y FIN")
print(f"La letra inicial es '{texto[0]}' y la letra final es '{texto[-1]}'")
print(" \n"," \n"," \n")
print("------------------------------------------------")
print(" \n"," \n"," \n")

print("TEXTO INVERTIDO")
print(f"Si ordenamos tu texto al revés va a decir: {texto_invertido}")
print(" \n"," \n"," \n")
print("------------------------------------------------")
print(" \n"," \n"," \n")
print("BUSCANDO LA PALABRA PYTHON")

if 'Python' in texto:
    print("La palabra 'Python' si se encuentra en el texto")
else:
    print("La palabra 'Python' no se encuentra en el texto")
print(" \n"," \n"," \n")
print("------------------------------------------------")