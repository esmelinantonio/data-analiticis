from pathlib import Path
guia = Path("Barcelona ","prueba.txt")
# print(guia)

base = Path.home()
guia = Path(base,"Barcelona","Sagrada_Familia")
# print(base)
# print(guia)

base = Path.home()
guia = Path(base,'Europa','España',Path('Barcelona','Sagrada_Familia'))
# print(base)
# print(guia)

base = Path.home()
guia = Path(base,"Europe","España",Path('Barcelona','Sagrada_Familia'))
# print(guia)

base = Path.home()
guia = Path(base,"Europe","España",Path('Barcelona','Sagrada_Familia'))
# print(guia.parent)

base = Path.home()
guia = Path(base,"Europe","España",Path('Barcelona','Sagrada_Familia'))
# print(guia.parent.parent)

guia = Path(Path.home(),"Europe")
for txt in Path(guia).glob("**/.txt"):
    print(txt)

guia = Path("Europe", "España", "Barcelona", "Prueba.txt")
en_europa = guia.relative_to(Path("Europe"))
en_espania = guia.relative_to(Path("Europe","España"))
print(en_europa)
print(en_espania)
