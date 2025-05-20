# Ejercicio 1: Gestión de Empleados (Métodos de Instancia)
class Empleado:
    def  __init__(self,nombre,apellido,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido
    
    def aplicar_aumento(self, porcentaje):
        self.salario += self.salario * porcentaje
        return int(self.salario)
    
    def obtener_salario(self):
        return self.salario
    
empleado_1 = Empleado('Juan', 'Perez', 50000)
print(empleado_1.nombre_completo())
print(empleado_1.obtener_salario())
print(empleado_1.aplicar_aumento(0.10))
print("\n---")
empleado_2 = Empleado('Pedro', 'Arroyo', 70000)
print(empleado_2.nombre_completo())
print(empleado_2.obtener_salario())
print(empleado_2.aplicar_aumento(0.14))