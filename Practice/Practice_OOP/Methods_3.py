# Ejercicio 3: Utilidades de Cadena de Texto (Métodos Estáticos)
class UtilidadesCadena:
    
    @staticmethod
    def invertir_cadena(cadena):
       return cadena[::-1]
    
    @staticmethod
    def es_palindromo(cadena):
        if cadena == cadena[::-1]:
            return True
        else:
            return False
    
    @staticmethod
    def contar_vocales(cadena):
        vocales = "aeiou"
        contador = 0
        for caracter in cadena:
            if caracter.lower() in vocales:
                contador += 1
        return contador
    
print("--- Invertir Cadena ---")
print(f"'Hola Mundo' invertida: {UtilidadesCadena.invertir_cadena('Hola Mundo')}")
print(f"'Python' invertida: {UtilidadesCadena.invertir_cadena('Python')}")

print("\n--- Es Palíndromo ---")
print(f"'oso' es palíndromo: {UtilidadesCadena.es_palindromo('oso')}")
print(f"'Ana' es palíndromo: {UtilidadesCadena.es_palindromo('Ana')}")
print(f"'La ruta natural' es palíndromo: {UtilidadesCadena.es_palindromo('La ruta natural')}")
print(f"'Python' es palíndromo: {UtilidadesCadena.es_palindromo('Python')}")
print(f"'reconocer' es palíndromo: {UtilidadesCadena.es_palindromo('reconocer')}")

print("\n--- Contar Vocales ---")
print(f"Numero de Vocales en 'Programacion': {UtilidadesCadena.contar_vocales('programacion')}")
print(f"Numero de Vocales en 'Murcielago': {UtilidadesCadena.contar_vocales('murcielago')}")
print(f"Numero de Vocales en 'aeiou': {UtilidadesCadena.contar_vocales('aeiou')}")
print(f"Numero de Vocales en 'XYZ': {UtilidadesCadena.contar_vocales('xyz')}")