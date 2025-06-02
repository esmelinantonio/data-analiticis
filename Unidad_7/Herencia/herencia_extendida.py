from operator import truediv


class Vertebrado:
    vertebrado = True
    

class Pez(Vertebrado):
    
    def nadar(self):
        print("Nadando...")
        
    def poner_huevos(self):
        print("Poner Huevos...")
    
class Ave(Vertebrado):
    tiene_pico = True
    
    def poner_huevos(self):
        print("Poner Huevos...")
        
class Reptil(Vertebrado):
    venenoso = True
    
class Mamifero(Vertebrado):
    
    def amamantar(self):
        print("Amamantando...")
        
    def caminar(self):
        print("Caminando...")
       
class Ornitorrinco(Pez,Ave,Reptil,Mamifero):
    pass

orni = Ornitorrinco()
print(f"El Ornitorrinco es vertebrado? {orni.vertebrado}")
print(f"El Ornitorrinco es venenoso? {orni.venenoso}")
orni.poner_huevos()
orni.nadar()
orni.amamantar()
orni.caminar()