from random import *
#----------------------------------------------------------------------

# Elegir la palabra
def elegir_palabra():
    palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
    palabra_secreta = choice(palabras)
    return palabra_secreta

#----------------------------------------------------------------------

# Ocultar palabra
def ocultar_palabra(palabra):
    longitud = len(palabra)
    ocultar = ["-"] * longitud
    return ocultar

#----------------------------------------------------------------------

# Pedir la letra
def pedir_letra():
    letra_usuario = input("Elige una letra: ").lower()
    return letra_usuario

#----------------------------------------------------------------------

# Actualizar Palabra
def actualizar_juego(letra_usuario,palabra_secreta,juego_actual):
    for indice,item in enumerate(palabra_secreta):
        if item == letra_usuario:
            juego_actual[indice] = letra_usuario
    return juego_actual

#----------------------------------------------------------------------

# Mostrar Juego Actualizado
def mostrar_juego_actual(juego_actual):
    return " ".join(juego_actual)

#----------------------------------------------------------------------

# Comprobar letra ingresada
def comprobar_letra_ingresada(letra_usuario):
    letras_validas = "abcdefghijklmnopqrstuvwxyz"
    valido = letra_usuario in letras_validas
    
    if not valido:
        print("Por favor digite una letra entre la (a - z)")
    return valido

#----------------------------------------------------------------------

# Verificar Estado del Juego
def verificar_ganador(juego_actual):
    has_ganado = "-" not in juego_actual
    return has_ganado

def verificar_perdedor(intentos):
    has_perdido = intentos <= 0
    return has_perdido

#----------------------------------------------------------------------

# Implementación del juego
letras_incorrectas = []
palabra_secreta = elegir_palabra()
juego_actual = ocultar_palabra(palabra_secreta)
intentos = 6

while intentos > 0:
    print("*" * 20 + "\n"*1)
    print(f"{mostrar_juego_actual(juego_actual)}")
    # Muestra si solo hay letras incorrectas
    if letras_incorrectas:
        print(f"Letras incorrectas: {len(letras_incorrectas)} ")
    else:
        print("Letras incorrectas:")
    print(f"Intentos: {intentos}")
    print("\n"*1)
    print("*" * 20 + "\n"*1)
    letra = pedir_letra()
    
    if not comprobar_letra_ingresada(letra):
       continue
    
    # Verificar si la letra no está en la palabra secreta
    if letra not in palabra_secreta:
        letras_incorrectas.append(letra)
        intentos -= 1
    else:
        juego_actual = actualizar_juego(letra, palabra_secreta, juego_actual)
       
    # Verificar si el jugador ha ha ganado
    if verificar_ganador(juego_actual):
        print(f"{mostrar_juego_actual(juego_actual)}")
        print("Felicitaciones, has encontrado la palabra!!!")
        break
           
    # Verificar si el jugador ha perdido
    if verificar_perdedor(intentos):
        print("Has agotado todos los intentos")
        print(f"La palabra oculta era {palabra_secreta}")
        break
            
    
    
   