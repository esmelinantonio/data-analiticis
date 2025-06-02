class Vehiculo:
    
     def __init__(self, marca, modelo, anio, kilometros):
         self.marca = marca
         self.modelo = modelo
         self.anio = anio
         self.kilometros = int(kilometros)
         
     def obtener_info(self):
         info = f"Vehículo: Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometros} km"
         return info
         
     def actualizar_kilometraje(self,nuevos_km):
         if nuevos_km > 0:
            self.kilometros += nuevos_km
 
 
class Coche(Vehiculo):
    def __init__(self, marca,modelo,anio,kilometraje,tipo_carroceria,numero_puertas):
        super().__init__(marca,modelo,anio,kilometraje)
        self.tipo_carroceria = tipo_carroceria
        self.numero_puertas = numero_puertas
        
    def obtener_info_coche(self):
        info = f"Vehículo: Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometros} km, Tipo de Carroceria: {self.tipo_carroceria}, N° de Puertas: {self.numero_puertas}"
        return info
    
    
    
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, kilometraje,capacidad_carga,tiene_remolque):
        super().__init__(marca,modelo,anio,kilometraje)
        self.capacidad_carga = capacidad_carga
        self.tiene_remolque = tiene_remolque
        
    def obtener_info_camion(self):
        info = f"Vehículo: Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometros} km, Capacidad de Carga: {self.capacidad_carga}, Tiene remolque: {self.tiene_remolque}"
        return info
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, kilometraje,cilindrada_cc, tipo_moto):
        super().__init__(marca,modelo,anio,kilometraje)
        self.cilindrada_cc = cilindrada_cc
        self.tipo_moto = tipo_moto
        
    def obtener_info_moto(self):
        info = f"Vehículo: Marca: {self.marca}, Modelo: {self.modelo}, Año: 202{self.anio}, Kilometraje: {self.kilometros} km, Cilindraje: {self.cilindrada_cc}, Tipo Moto: {self.tipo_moto}"
        return info
    
        
mi_coche = Coche('Toyota','Corolla','2022','35000','Sedán',4)
print("--- Mi Coche ---")
print(mi_coche.obtener_info())
print(mi_coche.obtener_info_coche())
mi_coche.actualizar_kilometraje(5000)
print(mi_coche.obtener_info())
print("\n---"*3)
mi_camion = Camion("Volvo", "FH16", 2019, 250000, 18, True)
print(mi_camion.obtener_info())
print(mi_camion.obtener_info_camion())
mi_camion.actualizar_kilometraje(10000)
print(mi_camion.obtener_info())
print("\n---"*3)
mi_moto = Motocicleta("Yamaha", "YZF-R6", 2023, 8000, 600, "Deportiva")
print(mi_moto.obtener_info())
print(mi_moto.obtener_info_moto())
    
    
    
    
    