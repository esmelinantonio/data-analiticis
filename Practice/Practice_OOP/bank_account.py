class Persona:
    
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    
    def __init__(self,nombre,apellido, numero_cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    def  imprimir_nombre(self):
        imprimir_nombre = f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"
        return imprimir_nombre
        
            
    
    
    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("Depósito aceptado")
        
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("fondos Insuficientes")
        
    
    
def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    print(cliente.imprimir_nombre())
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    opcion = ''
    
    while opcion != 'S':
        print("elije: Depositar (D), Retirar (R) o Salir (S)")
        opcion = input()
        
        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente.imprimir_nombre())
    print("Gracias por usar el banco")

inicio()