def describir_persona(nombre,**kwargs):
    print(f"Caractericticas de {nombre}")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
        
kwargs = {'color_ojos':'negro','color_cabello':'negro','color_piel':'moreno'}
print(describir_persona('Esmelin',**kwargs))