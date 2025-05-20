# Ejercicio 2: Creación de Formas Geométricas (Métodos de Clase)
class Rectangulo:
    
    unidades_predeterminadas = "cm" # atributo de clase
    
    def  __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        
    def area(self):
        calcular_area = self.ancho * self.alto
        return calcular_area
    
    @classmethod
    def crear_cuadrado(cls, lado):
        return cls(lado,lado)
    
    @classmethod
    def establecer_unidades(cls,nuevas_unidades):
        cls.unidades_predeterminadas = nuevas_unidades
        
rectangulo_normal = Rectangulo(5,10)
print(f'El area del rectangulo es: {rectangulo_normal.area()} {rectangulo_normal.unidades_predeterminadas}')

cuadrado = Rectangulo.crear_cuadrado(7)
print(f"Área del cuadrado es: {cuadrado.area()} {cuadrado.unidades_predeterminadas}")

