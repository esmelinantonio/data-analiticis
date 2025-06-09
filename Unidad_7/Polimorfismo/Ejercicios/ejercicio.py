

# palabra = "polimorfismo"
# lista = ["Clases", "POO", "Polimorfismo"]
# tupla = (1, 2, 3, 80)
#
# for pala in [palabra,lista,tupla]:
#     print(len(pala))
    
class Arquero:
    def atacar(self):
        print("Lanzar flecha")
    
    def defender(self):
        print("Esconderse")
        
class Mago:
    def atacar(self):
        print("Lanzar hechizo")
        
    def defender(self):
        print("Escudo mágico")
        
class Samurai:
    def atacar(self):
        print("Ataque con Katana")
        
    def defender(self):
        print("Bloqueo")
        
gandalf = Mago()
hawkeye = Arquero()
ishido = Samurai()

personajes = [gandalf,hawkeye,ishido]

for personaje in personajes:
    personaje.atacar()
    personaje.defender()
    
    
    