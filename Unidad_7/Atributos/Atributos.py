class Casa:
    def __init__(self,color, cantidad_pisos):
        self.color = color
        self.cantidad_pissos = cantidad_pisos
        
casa_blanca = Casa('Blanca', '4')
print(type(casa_blanca))
print(casa_blanca.cantidad_pissos)
print(casa_blanca.color)

# --------------------------------------------------
class Cubo:
    caras = 6
    
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo('rojo')
print(f"El cubo tiene {cubo_rojo.caras} caras y es de color {cubo_rojo.color}")