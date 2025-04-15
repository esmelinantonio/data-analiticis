mi_dic ={"curso":"python","clase":"Diccionarios"}
mi_dic["recursos"] = ["notas","Ejercicios"] # Agregar nuevos datos, o modificarlos
print(mi_dic)
print(mi_dic.keys())  # Acceso a valores a través del nombre de las claves
print(mi_dic.values()) # Acceso a valores a través del nombre de los valores
print(mi_dic.items()) # Acceso a valores a través del par, clave:valor
print(type(mi_dic))

mi_dic2 = {"clave1":"valor1","clave2":"valor2","clave3":"valor3","clave4":"valor4"}
print(mi_dic2)
valor = mi_dic2["clave1"] # Acceder a un valor de un diccionario por medio de su clave:
print(valor)

dic = {'clave1':55,'clave2':[10,20,30],'clave3':{'s1':100,'s2':200}}
print(dic['clave2'])
print(dic['clave2'][1]) # accedemos a uno de los elemento que se encuentra dentro de la lista asociada la clave 2

print(dic['clave3']['s2'])

dic_2 = {'clave1':['a','b','c'],'clave2':['d','e','f']}
print(dic_2['clave2'][1].upper())