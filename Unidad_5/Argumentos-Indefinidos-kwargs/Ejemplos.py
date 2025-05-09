# Recorremos las posiciones del diccionario formado por
# kwargs, e imprimimos sus claves y sus respectivos valores
def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

suma(x=3, y=5, z=2)

# Sumamos todos los valores e imprimimos en pantalla
def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))


def prueba(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}")
        
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        
prueba(15,20,100,200,300,400,x='uno',y="dos")


def prueba(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}")
        
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        
args = [100,200,300,400]
kwargs = {'x':'uno', 'y':'dos','z':'tres'}
prueba(5,5,*args,**kwargs)