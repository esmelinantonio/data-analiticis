products = ['Mouse', 'Keyboard','Monitor','Scanner']

dic_products = {
                'Mouse':(250.000,56,280),
                'Keyboard':(400.000,43,180),
                'Monitor':(680.000,67,200),
                'Scanner':(150.000,45,320)
                }

# imprime el total de unidades disponibles
total_unidades_Mouse = dic_products['Mouse'][1]
total_unidades_Keyboard = dic_products['Keyboard'][1]
total_unidades_Monitor =  dic_products['Monitor'][1]
total_unidades_Scanner =  dic_products['Scanner'][1]

total_inventario_Keyboard = dic_products['Keyboard'][0]
total_inventario_Monitor =  dic_products['Monitor'][0]
total_inventario_Scanner =  dic_products['Scanner'][0]
total_inventario_Mouse = dic_products['Mouse'][0]


total_unidades = total_unidades_Mouse+total_unidades_Monitor+total_unidades_Keyboard+total_unidades_Scanner
total_inventario = total_inventario_Mouse+total_inventario_Monitor+total_inventario_Keyboard+total_inventario_Scanner



print('Total Unidades Disponibles: ' ,total_unidades)
print('Precio total del Inventario: $' ,round(total_inventario, 2))