from pathlib import Path
ruta_base = Path.home()
print(ruta_base)
# -----------------------------------------------------
guia = Path("Curso Python","Ejercicios","Ejercicio2.py")
# print(guia)
ruta = guia.relative_to(Path("Curso Python","Ejercicios"))
print(ruta)
# -------------------------------------------------------------
guia = Path(ruta_base,"Curso Python","Ejercicios","Ejercicio3.py")
# print(guia)
ruta = guia.relative_to(Path(ruta_base,"Curso Python","Ejercicios"))
print(ruta)
# -------------------------------------------------------------------
