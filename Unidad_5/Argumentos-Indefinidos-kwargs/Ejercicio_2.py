
def lista_atributos(**kwargs):
    
    nueva = list(dict(**kwargs).values())
    return nueva

kwargs = {'nombre':'Pedro','apellido':'Sanchez','Edad':54}
print(lista_atributos(**kwargs))
