from turtledemo.chaos import jumpto


class Perro:
    def ladrar(self):
        print("¡Guau!")
pluto = Perro()
pluto.ladrar()
# ----------------------------------------
class Mascota:
    
    @classmethod
    def respirar(cls):
        print('Inhalar... Exhalar')

Mascota.respirar()
# -------------------------------------------
class Jugador:
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(f"El estado vivo del jugador es {Jugador.vivo}")
        
Jugador.revivir()
print(Jugador.vivo)
# -------------------------------------------
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        
    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(f"Te quedan {self.cantidad_flechas}")
        
robin_hood = Personaje(15)
robin_hood.lanzar_flechas()