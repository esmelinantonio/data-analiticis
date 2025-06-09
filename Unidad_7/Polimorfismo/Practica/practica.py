class Libro:
    def __init__(self,titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}" de {self.autor}'
    
    def __len__(self):
        return self.cantidad_paginas
    
    def __del__(self):
        print('Libro eliminado')
    
libro1 = Libro("Cien años de Soledad", 'Gabriel Garcia Márquez', 512)
print(str(libro1))
print(len(libro1))
del libro1